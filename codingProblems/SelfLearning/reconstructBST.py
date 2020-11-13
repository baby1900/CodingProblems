'''
Given the in-order and post-order traversal of a BST, reconstruct the tree

E.g: Given [1, 2, 3, 4, 5, 6, 7] as inorder and [1, 3, 2, 5, 7, 6, 4] as postorder, reconstruct the BST

'''


class Node:
  def __init__(self, data, left_child=None, right_child=None):
    self.data = data
    self.left_child = left_child
    self.right_child = right_child
    
  def inorder_traversal(self):
    if self.left_child:
      self.left_child.inorder_traversal()
    print(self.data)
    if self.right_child:
      self.right_child.inorder_traversal()
  
  def postorder_traversal(self):
    if self.left_child:
      self.left_child.postorder_traversal()
    if self.right_child:
      self.right_child.postorder_traversal()
    print(self.data)
    

def reconstruct_bst(inorder_t, postorder_t, inorder_t_start, inorder_t_end, postorder_t_start, postorder_t_end):
  if inorder_t_end < inorder_t_start:
    return None
  if inorder_t_end == inorder_t_start:
    return Node(inorder_t[inorder_t_end])
  root_value = postorder_t[postorder_t_end]
  root = Node(root_value)
  inorder_index = inorder_t.index(root_value)
  post_index = 0
  for index, value in enumerate(postorder_t):
    if value > root_value:
      post_index = index
      break
  root.left_child = reconstruct_bst(inorder_t, postorder_t, inorder_t_start, inorder_index - 1, postorder_t_start, post_index - 1)
  root.right_child = reconstruct_bst(inorder_t, postorder_t, inorder_index + 1, inorder_t_end, post_index, postorder_t_end - 1)
  return root