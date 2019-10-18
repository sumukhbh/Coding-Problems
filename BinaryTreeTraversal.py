# Binary Tree Traversals recursive Implementation #

class Node(object):
    def __init__(self,val):
        self.root = val
        self.left = None
        self.right = None


def preorder(root_val):
    if root_val:
        print(root_val.root)
        if root_val.left:
            preorder(root_val.left)
        if root_val.right:
            preorder(root_val.right)

def inorder(root_val):
    if root_val:
        if root_val.left:
            inorder(root_val.left)
        print(root_val.root)
        if root_val.right:
            inorder(root_val.right)

def postorder(root_val):
    if root_val:
        if root_val.left:
            postorder(root_val.left)
        if root_val.right:
            postorder(root_val.right)
        print(root_val.root)



rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(4)
rootNode.left.right = Node(5)
rootNode.right.left = Node(6)
rootNode.right.right = Node(7)

print("Preorder Traversal:")
preorder(rootNode)
print("\n")
print("Inorder Traversal:")
inorder(rootNode)
print("\n")
print("Postorder Traversal:")
postorder(rootNode)







    





