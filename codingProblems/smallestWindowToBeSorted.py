'''Given an array of integers that are out of roder
determine the bounds of the smallest window
that must be sorted in order for the entire array to be sorted.
For example, given [3,7,5,6,9], you should return (1,3)
'''

def findWindow(inarr):
    smallestElement = inarr[-1]
    greatestElement = inarr[0]
    left, right = None, None
    for i in range(0, len(inarr)):
        greatestElement = max(inarr[i], greatestElement)
        if inarr[i] < greatestElement:
            right = i
    for i in range(len(inarr) - 1, -1, -1):
        smallestElement = min(inarr[i], smallestElement)
        if inarr[i] > smallestElement:
            left = i
    return(left, right)

assert findWindow([2,3,1,6,5]) == (0,4)

