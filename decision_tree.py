import collections
from math import log
import operator
import copy


def calcShannonEnt(dataSet):

    numEntries = len(dataSet)

    labelCounts = collections.defaultdict(int)

    for featVec in dataSet:
        currentLabel = featVec[-1]
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSetForSeries(dataSet, axis, value):

    eltDataSet = []
    gtDataSet = []
    for feat in dataSet:
        if feat[axis] <= value:
            eltDataSet.append(feat)
        else:
            gtDataSet.append(feat)

    return eltDataSet, gtDataSet


def splitDataSet(dataSet, axis, value):

    retDataSet = []

    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet


def calcInfoGainForSeries(dataSet, i, baseEntropy):
    maxInfoGain = 0.0
    bestMid = -1
    featList = [example[i] for example in dataSet]

    classList = [example[-1] for example in dataSet]

    dictList = dict(zip(featList, classList))

    sortedFeatList = sorted(dictList.items(), key=operator.itemgetter(0))

    numberForFeatList = len(sortedFeatList)

    midFeatList = [round((sortedFeatList[i][0] + sortedFeatList[i + 1][0]) / 2.0, 3) for i in
                   range(numberForFeatList - 1)]

    for mid in midFeatList:
        eltDataSet, gtDataSet = splitDataSetForSeries(dataSet, i, mid)

        newEntropy = len(eltDataSet) / len(sortedFeatList) * calcShannonEnt(eltDataSet) + len(
            gtDataSet) / len(sortedFeatList) * calcShannonEnt(gtDataSet)

        infoGain = baseEntropy - newEntropy
        if infoGain > maxInfoGain:
            bestMid = mid
            maxInfoGain = infoGain

    return maxInfoGain, bestMid


def calcInfoGain(dataSet, featList, i, baseEntropy):

    uniqueVals = set(featList)

    newEntropy = 0.0
    for value in uniqueVals:
        subDataSet = splitDataSet(dataSet=dataSet, axis=i, value=value)
        prob = len(subDataSet) / float(len(dataSet))
        newEntropy += prob * calcShannonEnt(subDataSet)
    infoGain = baseEntropy - newEntropy

    return infoGain


def chooseBestFeatureToSplit(dataSet, labels):

    numFeatures = len(dataSet[0]) - 1

    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0

    bestFeature = -1

    flagSeries = 0

    bestSeriesMid = 0.0


    for i in range(numFeatures):

        featList = [example[i] for example in dataSet]

        if isinstance(featList[0], str):
            infoGain = calcInfoGain(dataSet, featList, i, baseEntropy)
        else:
            infoGain, bestMid = calcInfoGainForSeries(dataSet, i, baseEntropy)

        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

            flagSeries = 0

            if not isinstance(dataSet[0][bestFeature], str):
                flagSeries = 1
                bestSeriesMid = bestMid

    if flagSeries:
        return bestFeature, bestSeriesMid
    else:
        return bestFeature


def createDataSet(dataSet,labels):

    labels_full = {}

    for i in range(len(labels)):
        labelList = [example[i] for example in dataSet]
        uniqueLabel = set(labelList)
        labels_full[labels[i]] = uniqueLabel

    return dataSet, labels, labels_full


def majorityCnt(classList):

    classCount = collections.defaultdict(int)

    for vote in classList:
        classCount[vote] += 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def createTree(mydataSet, mylabels):
    dataSet =  copy.deepcopy(mydataSet)
    labels = copy.deepcopy(mylabels)
    classList = [example[-1] for example in dataSet]

    if classList.count(classList[0]) == len(classList):
        return classList[0]

    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet=dataSet, labels=labels)

    bestFeatLabel = ''
    flagSeries = 0

    midSeries = 0.0

    if isinstance(bestFeat, tuple):
        bestFeatLabel = str(labels[bestFeat[0]]) + ' less_than ' + str(bestFeat[1]) + ' ?'
        midSeries = bestFeat[1]
        bestFeat = bestFeat[0]
        flagSeries = 1
    else:
        bestFeatLabel = labels[bestFeat]
        flagSeries = 0
    myTree = {bestFeatLabel: {}}

    featValues = [example[bestFeat] for example in dataSet]

    if flagSeries:
        eltDataSet, gtDataSet = splitDataSetForSeries(dataSet, bestFeat, midSeries)
        subLabels = labels[:]
        subTree = createTree(eltDataSet, subLabels)
        myTree[bestFeatLabel]['yes'] = subTree
        subTree = createTree(gtDataSet, subLabels)
        myTree[bestFeatLabel]['no'] = subTree

        return myTree

    else:

        del (labels[bestFeat])
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]
            subTree = createTree(splitDataSet(dataSet=dataSet, axis=bestFeat, value=value),
                                 subLabels)
            myTree[bestFeatLabel][value] = subTree
        return myTree



