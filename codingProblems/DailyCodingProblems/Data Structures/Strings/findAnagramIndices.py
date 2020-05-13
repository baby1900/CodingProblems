"""
Given a word w and a string s, find all indices in s which are the starting location of anagrams of w.

For example, given w is ab and s is abxaba, return [0,3,4]
"""

from collections import defaultdict


def findAnagramIndices(w, s):
    wDict = {}
    wLen = len(w)
    sLen = len(s)
    readingDict = {}
    startPos = -1
    result = []
    for i in range(wLen):
        wChar = w[i]
        if wChar in wDict:
            wDict[wChar] += 1
        else:
            wDict[wChar] = 1
    for j in range(sLen):
        readLength = j - startPos
        sChar = s[j]
        if sChar not in wDict:
            readingDict.clear()
            startPos = j
        else:
            if sChar not in readingDict:
                readingDict[sChar] = 1
            else:
                readingDict[sChar] += 1
            if readLength == wLen:
                if readingDict == wDict:
                    result.append(startPos + 1)
                readingDict[s[startPos + 1]] -= 1
                startPos += 1
    return result


###better solution:


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]


def better_FindAnagramIndices(w, s):
    result = []
    wDict = defaultdict(int)
    for char in w:
        wDict[char] += 1
    for char in s[:len(w)]:
        wDict[char] -= 1
        del_if_zero(wDict, char)
    if not wDict:
        result.append(0)
    for i in range(len(w), len(s)):
        start_char, end_char = s[i - len(w)], s[i]
        wDict[start_char] += 1
        del_if_zero(wDict, start_char)
        wDict[end_char] -= 1
        del_if_zero(wDict, end_char)
        if not wDict:
            result.append(i - len(w) + 1)
    return result
