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
def height(root):
    if root is None:
        return 0
    else:
        left = height(root.left)
        right = height(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1
def levelOrder(root):
    h = height(root)
    print("Height = : ", h)
    for ii in range(1, h+1):
        printGivenLevel(root, ii)
def printGivenLevel(root, level):
    if root is None:
        return None
    if level == 1:
        print(root.info, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level - 1)
def check_binary_search_tree_1(root):
    if root is None:
        return
    else:
        if root.left:
            print("\n", root.left.info, ":", root.info)
            if root.left.info < root.info:
                check_binary_search_tree_1(root.left)
            else:
                return False
        if root.right:
            print("\n", root.right.info, ":", root.info)
            if root.right.info > root.info:
                check_binary_search_tree_1(root.right)
            else:
                return False
        if root.left is None and root.right is None:
            print("\n....here", root.info)
            return True

    return True


flag = True
pre = -1  # As all data are >= 0 so set pre = -1
def inOrder(root):
    global flag, pre
    if root.left:
        inOrder(root.left)
    if pre < root.info:
        pre = root.info
    else:
        flag = False
        return
    if root.right:
        inOrder(root.right)
def check_binary_search_tree_(root):
    inOrder(root)
    global flag
    return flag

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
print(check_binary_search_tree_(tree.root))