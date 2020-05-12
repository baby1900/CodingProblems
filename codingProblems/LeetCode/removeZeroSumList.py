"""
Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list,
we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.
You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, nextnode=None):
        self.val = val
        self.next = nextnode

    def append(self, value):
        currnode = self
        if currnode is None:
            currnode.val = value
        else:
            while currnode.next != None:
                currnode = currnode.next
            currnode.next = ListNode(value)

def removeZeroSumSublists(head: ListNode) -> ListNode:
    resultHead = currNode = ListNode(0)
    resultHead.next = head
    accSumDict = {}
    accSum = 0
    while currNode is not None:
        accSum += currNode.val
        if accSum in accSumDict:
            currNode = accSumDict[accSum].next
            tempSum = accSum + currNode.val
            while tempSum != accSum and tempSum in accSumDict:
                del accSumDict[tempSum]
                currNode = currNode.next
                tempSum += currNode.val
            accSumDict[accSum].next = currNode.next
        else:
            accSumDict[accSum] = currNode
        currNode = currNode.next
    return resultHead.next

