""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root is None:
        return
    else:
        if root.left:
            if root.left.data < root.data:
                check_binary_search_tree_(root.left)
            else:
                return False
        if root.right:
            if root.right.data > root.data:
                check_binary_search_tree_(root.right)
            else:
                return False
        return True




