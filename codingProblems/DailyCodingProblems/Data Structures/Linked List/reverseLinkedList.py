# Class definition of a linked list
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next


# Reverse a linked list
def reverse_linked_list(node):
    prev_node = None
    curr_node = node
    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node
    