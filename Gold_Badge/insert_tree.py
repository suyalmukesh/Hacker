class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def preorder_leaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.info, end=" ")
    preorder_leaves(root.left)
    preorder_leaves(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        root = self.root
        while True:
            if val > root.info:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(val)
                    break
            elif val < root.info:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            else:
                break






# Enter you code here.

tree = BinarySearchTree()
#t = int(input())
t = 5
#arr = list(map(int, input().split()))
arr = [890, 325, 290, 530, 965]
for i in range(t):
    tree.insert(arr[i])

print("\nPre-Order")
preOrder(tree.root)
print("\nPre order leaves")
preorder_leaves(tree.root)