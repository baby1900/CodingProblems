"""
Given a sorted list of integers of length N,
determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.
Do this in O(log N) time.
"""
import random

# findElement([1, 2, 3, 4, 5], 0, 4, 3) -> True
# findElement([1, 2, 3, 4, 5], 0, 4, 6) -> False
def findElement(arr, start, end, element):
    N = end - start + 1
    if N == 1:
        return element == arr[0]
    pivotIndex = random.randint(0, N - 1) + start
    if element == arr[pivotIndex]:
        return True
    elif element < arr[pivotIndex]:
        return findElement(arr, 0, pivotIndex, element)
    else:
        return findElement(arr, pivotIndex, end, element)


assert(findElement([1, 2, 3, 4, 5], 0, 4, 3))
