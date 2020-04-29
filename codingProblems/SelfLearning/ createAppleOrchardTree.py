"""
A girl is walking along an apple orchard with a bag in each hand.

She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5],
the longest portion will involve types 1 and 3, with a length of four.

"""


def createAppleOrchardTree(trees):
    startpos = lastkind = maxlength = 0
    twoKindLastOccurDict = {}
    for currpos in range(len(trees)):
        currkind = trees[currpos]
        if len(twoKindLastOccurDict) == 2 and currkind not in twoKindLastOccurDict:
            maxlength = max(maxlength, currpos - startpos)
            startpos = currpos
            for item in twoKindLastOccurDict:
                startpos = min(startpos, twoKindLastOccurDict[item])
            startpos += 1
            twoKindLastOccurDict.clear()
            twoKindLastOccurDict[lastkind] = currpos - 1
        twoKindLastOccurDict[currkind] = currpos
        lastkind = currkind
    return maxlength


print(createAppleOrchardTree([2, 1, 2, 3, 3, 1, 3, 5]))