# Class definition of a linked list
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

    def length(self):
        if not self.next:
            return 0
        return 1 + self.next.length()

# Find intersecting nodes of linked lists
def intersection(node0, node1):
    m, n = node0.length(), node1.length()
    curr_node0, curr_node1 = node0, node1
    print(curr_node0.data)

    if (m > n):
        for _ in range(m - n):
            curr_node0 = curr_node0.next
    else:
        for _ in range(n - m):
            curr_node1 = curr_node1.next
    
    while curr_node0.data != curr_node1.data:
        curr_node0 = curr_node0.next
        curr_node1 = curr_node1.next
    
    return curr_node0
 

s = Node(1)
s.next = Node(2)
s.next.next = Node(3)


t = Node(2)
t.next = Node(2)
t.next.next = Node(3)

aa = intersection(s, t)
print(aa.data, aa.next.data)