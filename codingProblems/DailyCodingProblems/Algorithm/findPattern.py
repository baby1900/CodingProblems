'''
Boyer-Moore string matching
'''

def createIndexDict(pattern: str):
    N = len(pattern)
    patternCharDict = {}
    for char in pattern:
        if char not in patternCharDict:
            for patternIndex in range(N - 1, -1, -1):
                if pattern[patternIndex] == char:
                    patternCharDict[char] = patternIndex
                    break
    return patternCharDict

def determineJump(patternIndex: int, indexDict: {}, charToFind: str):
    if charToFind in indexDict:
        return patternIndex - indexDict[charToFind]
    else:
        return patternIndex + 1

def findPattern(text: str, pattern:str):
    N = len(text)
    M = len(pattern)
    indexDict = createIndexDict(pattern)
    textIndex = 0
    while textIndex <= N - M:
        for patternIndex in range(M - 1, -1, -1):
            if text[textIndex + patternIndex] != pattern[patternIndex]:
                break
        if patternIndex == 0:
            return textIndex
        else:
            textIndex += max(1, determineJump(patternIndex, indexDict, text[textIndex]))
    return False

assert (findPattern("abcsdagdfads", "agd")) == 5