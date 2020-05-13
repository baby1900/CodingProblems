"""Given an array of integers, return a new array such
that each elemnt at index i of the new array is the product of all
the numbers in the original array expect the one at i
This Solution runs in O(n) time and O(n) space
"""


def products(nums):
    inorderProduct = []
    reverseProduct = []
    outarr = []
    for num in nums:
        if inorderProduct:
            inorderProduct.append(inorderProduct[-1] * num)
        else:
            inorderProduct.append(num)
    for num in reversed(nums):
        if reverseProduct:
            reverseProduct.append(reverseProduct[-1] * num)
        else:
            reverseProduct.append(num)
    reverseProduct.reverse()
    for i in range(len(nums)):
        if i == 0:
            outarr.append(reverseProduct[1])
        elif i == len(nums) - 1:
            outarr.append(inorderProduct[i - 1])
        else:
            outarr.append(inorderProduct[i - 1] * reverseProduct[i + 1])
    return outarr


assert products([1,2,3,4]) == [24,12,8,6]
