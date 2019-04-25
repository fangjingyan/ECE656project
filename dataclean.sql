-- Part 1.1.1 Time Checks
-- 1. anything can not occur before yelp-founded time or from the future
-- (including review time, elite time, tip time, user start time)
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

-- 2. review can not be left before the user account is created
delete
from review_clean
where review_clean.review_id in
      (select review_clean.review_id
       from (user_clean
              inner join review_clean using (user_id))
       where user_clean.yelping_since > review_clean.date
       group by user_clean.user_id);

-- 3. a user can not become an elite member before becoming a yelp user
delete
from user_clean
where user_id in
      (SELECT user_clean.user_id
       FROM (user_clean
              INNER JOIN user_elite_clean using (user_id))
       WHERE YEAR(user_clean.yelping_since) > user_elite_clean.year
       GROUP BY user_clean.user_id);

delete
from user_elite_clean
where user_id in
      (SELECT user_clean.user_id
       FROM (user_clean
              INNER JOIN user_elite_clean using (user_id))
       WHERE YEAR(user_clean.yelping_since) > user_elite_clean.year
       GROUP BY user_clean.user_id);


-- Part 1.1.2 Logical Consistency Checks
-- 1. id check, id cannot be null in all tables
delete
from review_clean
where business_id in
      (select review_clean.business_id
       from review_clean
              left join business_clean using (business_id)
       where business_clean.business_id is null);

delete
from review_clean
where user_id in
      (select review_clean.user_id
       from review_clean
              left join user_clean using (user_id)
       where user_clean.user_id is null);
delete
from user_elite_clean
where user_id in
      (select user_elite_clean.user_id
       from user_elite_clean
              left join user_clean using (user_id)
       where user_clean.user_id is null);

-- 2. user's review_count should not be less than those review sum in the review table
delete
from user_clean
where user_id in
      (select user_clean.user_id
       from user_clean
              inner join (select count(user_id) as countedReviews, user_id
                          from review_clean
                          group by user_id) as r using (user_id)
       where r.countedReviews > review_count);

-- Part 1.2 Representative Limit
-- 1. filter users whose review_count < a threshold out
delete from user_clean where review_count < 2;

-- 2. filter users whose average ratings = 5 or 0
delete from user_clean where average_stars =5 or average_stars = 0;
