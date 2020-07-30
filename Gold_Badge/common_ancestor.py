# This was pretty easy implementation but thinking was bit complicated
# Dated : 20/07/2020
##########################################################
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
        if self.root is None:
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
# Small but pretty good thinking
# How I reached conclusion see at end
def lca(root, v1, v2):
    if v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    elif v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)
    else:
        return root


# Enter your code here
tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
v = list(map(int, input().split()))
ans = lca(tree.root, v[0], v[1])
print(ans.info)

#####################################################
# def lca(root, v1, v2):
#    print("root v1 v2 ",root.info, v1, v2)
#    if v1 == root.info or v2 == root.info:
#        return root
#    elif root.left and not root.right:
#        return root
#    elif not root.left and root.right:
#        return root
#    elif v1 < root.info < v2:
#        return root
#    elif v1 > root.info > v2:
#        return root
#    elif v1 < root.info and v2 < root.info:
#        lca(root.left,v1,v2)
#    elif v1 > root.info and v2 > root.info:
#        lca(root.right, v1, v2)
#####################################################

