"""
Given an array of integers, return a new array where each element in the new array is the number of
smaller elements to the right of that element in the original input array

For example, given the array [3,4,9,6,1], return [1,1,2,1,0]
"""
import bisect


def smaller_counts(lst):
    n = len(lst)
    if n == 1:
        return [0]
    result = [0 for i in range(n)]
    for pos in range(n - 2, -1, -1):
        for currpos in range(pos + 1, n):
            if lst[pos] > lst[currpos]:
                result[pos] = result[currpos] + 1
                break
    return result


def better_smaller_counts(lst):
    result = []
    seen = []
    for item in reversed(lst):
        smaller_count = bisect.bisect_left(seen, item)
        result.append(smaller_count)
        bisect.insort(seen, item)
    return reversed(result)
