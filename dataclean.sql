--  Part 1.1.1 Time Checks
--  1. anything can not occur before yelp-founded time or from the future
--  (including review time, elite time, tip time, user start time)
delete
from review_clean
where date < '2004-10-01' || date > '2018-04-30';

delete
from user_elite_clean
where year < 2004 || year > 2018;

delete
from tip_clean
where date < '2004-10-01' || date > '2018-04-30';

delete
from user_clean
where yelping_since < '2004-10-01' || yelping_since > '2018-04-30';

--  2. review can not be left before the user account is created
delete
from review_clean
where review_id in
      (select r.review_id
       from (user_clean
              inner join (select * from review_clean) as r using (user_id))
       where user_clean.yelping_since > r.date
       group by user_clean.user_id);

--  3. a user can not become an elite member before becoming a yelp user
delete
from user_clean
where user_id in
      (SELECT u.user_id
       FROM ((select * from user_clean) as u
              INNER JOIN user_elite_clean using (user_id))
       WHERE YEAR(u.yelping_since) > user_elite_clean.year);

delete
from user_elite_clean
where user_id in
      (SELECT user_clean.user_id
       FROM (user_clean
              INNER JOIN (select * from user_elite_clean) as ue using (user_id))
       WHERE YEAR(user_clean.yelping_since) > ue.year
       GROUP BY user_clean.user_id);


--  Part 1.1.2 Logical Consistency Checks
--  1. id check, id cannot be null in all tables
delete
from review_clean
where business_id in
      (select r.business_id
       from (select * from review_clean) as r
              left join business_clean using (business_id)
       where business_clean.business_id is null);

delete
from review_clean
where user_id in
      (select r.user_id
       from (select * from review_clean) as r
              left join user_clean using (user_id)
       where user_clean.user_id is null);

delete
from user_elite_clean
where user_id in
      (select ue.user_id
       from (select * from user_elite_clean) as ue
              left join user_clean using (user_id)
       where user_clean.user_id is null);
--  2. user's review_count should not be less than those review sum in the review table
delete
from user_clean
where user_id in
      (select u.user_id
       from (select * from user_clean) as u
              inner join (select count(user_id) as countedReviews, user_id
                          from review_clean
                          group by user_id) as r using (user_id)
       where r.countedReviews > review_count);




-- primary keys
alter table business_clean
  add constraint business_clean_pk primary key (business_id);
alter table review_clean
  add constraint review_clean_pk
    primary key (review_id);
alter table user_clean
  add constraint user_clean_pk
    primary key (user_id);
alter table user_elite_clean
  add constraint user_elite_clean_pk
    primary key (user_id, year);

-- foreign keys
set foreign_key_checks = 0;
alter table business_categories_clean
  add constraint business_categories_clean_business_clean_business_id_fk
    foreign key (business_id) references business_clean (business_id);

set foreign_key_checks = 0;
alter table review_clean
  add constraint review_clean_business_clean_business_id_fk
    foreign key (business_id) references business_clean (business_id);

alter table review_clean
  add constraint review_clean_user_clean_user_id_fk
    foreign key (user_id) references user_clean (user_id);

set foreign_key_checks = 0;
alter table user_elite_clean
  add constraint user_elite_clean_user_clean_user_id_fk
    foreign key (user_id) references user_clean (user_id);

