import os
import sys

class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        # Root -> Left -> right
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self,root):
        # Left -> Right -> Root
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    def find_deepest_right(self, root):
        if root:
            if root.right is None:
                return root.data
            else:
                self.find_deepest_right(self, root.right)
        else:
            return None
        return 0

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            # if root node to be deleted
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode()

            root.data = temp.data

            root.right = self.delete(root.right, temp.data)
        return root

    def minValueNode(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

root = node(10)
root.printTree()
print("\n")
root.insert(5)
root.insert(500)
root.insert(-1)
root.printTree()
print("\n")
root.insert(100)
root.printTree()
print("\n")
print("\nInorder Traversal ")
print(root.inorderTraversal(root))
print("\nPre_order Traversal")
print(root.preorderTraversal(root))
print("\nPost_order Traversal")
print(root.postorderTraversal(root))
root.delete(root,5)
print(root.postorderTraversal(root))
root.insert(-12)
root.printTree()
print("\n")
root.insert(5)
root.insert(500)
root.printTree()
print("\n")
root.delete(root,500)
root.printTree()