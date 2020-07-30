# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Recursive function to do a pre-order traversal of the tree and fill the dictionary
# Here node has 'dist' horizontal distance from the root of the
# tree and level represent level of the node
def printTop(root, dist, level, dict):
    # base case: empty tree
    if root is None:
        return

    # if current level is less than maximum level seen so far
    # for the same horizontal distance or horizontal distance
    # is seen for the first time, update the dictionary
    if dist not in dict or level < dict[dist][1]:
        # update value and level for current distance
        dict[dist] = (root.key, level)

    # recur for left subtree by decreasing horizontal distance and
    # increasing level by 1
    printTop(root.left, dist - 1, level + 1, dict)

    # recur for right subtree by increasing both level and
    # horizontal distance by 1
    printTop(root.right, dist + 1, level + 1, dict)


# Function to print the top view of given binary tree
def printTopView(root):
    # create a dictionary where
    # key -> relative horizontal distance of the node from root node and
    # value -> pair containing node's value and its level
    dict = {}

    # do pre-order traversal of the tree and fill the dictionary
    printTop(root, 0, 0, dict)
    print("Dict", dict)
    # traverse the sorted map (base on keys) and print top view
    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printTopView(root)

