# Very Tough for me
# Copied the code from somewhere
# Need to understand it more
# Dated : 22/07/2020
############################################

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def printTop(root, dist, level, dict):
    if root is None:
        return
    if dist not in dict or level < dict[dist][1]:
        dict[dist] = (root.info, level)

    printTop(root.left, dist - 1, level + 1, dict)
    printTop(root.right, dist + 1, level + 1, dict)


def topView(root):
    dict = {}
    printTop(root, 0, 0, dict)

    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)