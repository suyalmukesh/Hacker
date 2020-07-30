import os
import sys
#sys.setrecursionlimit(10**4)
def debug(text):
    print(f"*** {text} ***")
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None
def insert(root, node):
    debug("Reached insert")
    if root is None:
       root = node
    else:
        debug("Root exists")
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        elif node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
def inorder(root):
    # Left -> Root -> Right
    if root:
        inorder(root.left)
        print(root.data, end="  ")
        inorder(root.right)
def preorder(root):
    # Root -> Left -> Right
    if root:
        print(root.data, end="  ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    # Left -> Right -> Root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="  ")
def minValueNode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current
def delete(root, key):
    debug("Inside DELETE")
    print("root", root.data,"key", key)
    # key is at leaf node
    if root is None:
        return root
    if key < root.data:
        debug("going left")
        root.left = delete(root.left, key)
    elif key > root.data:
        debug("going right")
        root.right = delete(root.right, key)

    if key == root.data:
        print("key == root == ", key)
        # case 1 : Node is Leaf node
        if root.left is None and root.right is None:
            debug("Leaf node to be deleted")
            root = None
            debug(inorder(root))
        # case 2 : Node has only one child
        elif root.left is None:
            debug("Only right child")
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            debug("Only left child")
            temp = root.left
            root = None
            return temp
        else:
        # case 3 : Node has both children
            debug("Has both the children")
            temp = minValueNode(root.right)
            root = temp
    return root
def print_all_leaves_leftToRight(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end="  ")
        else:
            if root.left:
                print_all_leaves_leftToRight(root.left)
            if root.right:
                print_all_leaves_leftToRight(root.right)
    else:
        print("No Root")
def print_tree(root):
    print("-----------------------")
    print("Pre-Order")
    preorder(root)
    print("\nIn-Order")
    inorder(root)
    print("\nPost-Order")
    postorder(root)
    print("\n-----------------------")
def height(Root):
    if Root is None:
        return 0
    else:
        left_tree  = height(Root.left)
        right_tree = height(Root.right)

        if left_tree > right_tree:
            return left_tree + 1
        else:
            return right_tree + 1
def height2(root):
    #BInary Tree , need to test further
    if root is None:
        return -1
    return max(1 + height(root.left), 1 + height(root.right))
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

def topview(root):
    if root.left:
        topview(root.left)
        print(root.data, end=" ")
        topview(root.right)

def find_parent(root):
    # find parent of each node
    lst = []
    if root.left:
        print(root.left.data, root.data)
        pair = (root.left.data, root.data)
        lst.append(pair)
        find_parent(root.left)
    if root.right:
        print(root.right.data, root.data)
        find_parent(root.right)

def find_common_ancestor(root, key1, key2):
    if root:
        if root.data == key1 or root.data == key2:
            parent = -1
        if key1 < root.data:
            print("In progress")






if __name__ == '__main__':
# Driver program to test the above functions
# Let us create the following BST
#      50
#    /     \
#   30      70
#   /  \   /  \
#  20  40 60  80
    ind = int(input("1 for default 2 for manual : "))
    if ind == 2:
        root = int(input("Enter Root : "))
        root = Node(root)

        while 1:
            n = int(input("\nEnter \n1->Insert \n2->search \n3->display \n4->delete\n5->leaves"
                          " \n6->Height \n7->Parents\n0->Quit\n"))
            if n == 1:
                num = int(input("Enter a number : "))
                insert(root, Node(num))
            if n == 2:
                key = int(input("Enter num to be deleted : "))
                result = search(root, key)
                if not result:
                    print("Not found ", key)
                else:
                    print("Found : ", result.data)
            if n == 3:
                print_tree(root)
            if n == 4:
                key = int(input("Enter num to be deleted : "))
                delete(root, key)
            if n == 5:
                print_all_leaves_leftToRight(root)
            if n == 6:
                print("Height = ", height(root))
            if n == 7:
                print("Parents of each node")
                find_parent(root)
            if n == 0:
                print("*** Quiting *** ")
                exit()
    if ind == 1:
        root = Node(50)
        insert(root, Node(30))
        insert(root, Node(20))
        insert(root, Node(40))
        insert(root, Node(70))
        insert(root, Node(60))
        insert(root, Node(80))
        print("Print Tree in all 3 orders \n")
        print_tree(root)
        print("Print leaves from left to right \n")
        print_all_leaves_leftToRight(root)
        print("\nHeight of Tree : ", height(root), "\n")
        print("\nTop Right View : ")
        topview(root)
        print("\nParent")
        find_parent(root)
        print(check_binary_search_tree_(root))



