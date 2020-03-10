"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array
For example, given [34, -50, 42, 14, -5, 86]
return 137 since we take 42, 14, -5, and 86
This algorithm is known as Kadane's algorithm
it runs in O(n) time and O(1) space
"""


def max_subarray_sum(arr):
    max_end_here = max_so_far = -float("inf")
    for num in arr:
        max_end_here = max(num, max_end_here + num)
        max_so_far = max(max_end_here, max_so_far)
    return max_so_far


assert max_subarray_sum([34, -50, 42, 14, -5, 86]) == 137
