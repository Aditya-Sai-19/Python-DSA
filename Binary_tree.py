
# Creating a Binary Tree
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None

# creating the tree nodes
drinks=Node("drinks")
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

# creating the links between the nodes
drinks.left = hot
drinks.right = cold
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta

# Creating a function that takes Node(Root) as input performs Preorder Traversal

def preorder(Node):
    if Node == None:
        return
    print(Node.val , end = " ")
    preorder(Node.left)
    preorder(Node.right)
print("Preorder Traversal\n-----------------------------------------")
preorder(drinks)
print("\n-------------------------------------------")

#Creating a function that takes Node(Root) as input and performs Inorder Traversal

def inorder(Node):
    if Node == None:
        return
    inorder(Node.left)
    print(Node.val , end = " ")
    inorder(Node.right)

print("Inorder Traversal\n-----------------------------------------")
inorder(drinks)
print("\n-------------------------------------------")

#Creating a function that takes Node(Root) as input and performs Postorder Traversal

def postorder(Node):
    if Node == None:
        return
    postorder(Node.left)
    postorder(Node.right)
    print(Node.val , end = " ")

print("Postorder Traversal\n-----------------------------------------")
postorder(drinks)
print("\n-------------------------------------------")