# Class definition of a linked list
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next


# Wiggle sort linked lists
def wiggle_sort(node):
    prev_node = node
    curr_node = node.next

    while curr_node:
        if prev_node.data > curr_node.data:
            prev_node.data, curr_node.data = curr_node.data, prev_node.data

        if not curr_node.next:
            break

        if curr_node.next.data > curr_node.data:
            print(111)
            curr_node.next.data, curr_node.data = curr_node.data, curr_node.next.data
            print()
        
        prev_node = curr_node.next
        curr_node = curr_node.next.next

    return node

s = Node(1)
s.next = Node(2)
s.next.next = Node(3)

tt = wiggle_sort(s)
print(tt.data, tt.next.data, tt.next.next.data)