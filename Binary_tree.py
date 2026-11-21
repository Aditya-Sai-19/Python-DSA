
from collections import deque

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

# Finding the height of the Binary Tree [ Using DFS ]

def DFSHeight(Node):
    if Node == None:
        return 0
    LH = DFSHeight(Node.left)
    RH = DFSHeight(Node.right)
    height = 1 + max(LH,RH)
    return height

h1 = DFSHeight(drinks)

print(f"Height of the Binary tree using DFS is : {h1}")
print("-------------------------------------------")

# Finding the height of the Binary Tree [ Using BFS ]

def BFSHeight(Node):
    queue = deque()
    height = 0
    queue.append(Node)
    while len(queue)!=0:
        level_size = len(queue)  # here level_size is the number of node in that specific level
        height += 1
        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height

h2 = BFSHeight(drinks)
print(f"Height of the Binary tree using BFS is : {h2}")
print("-------------------------------------------")

# Find the diameter of the Binary Tree

def diameter(Node):

    LongestDepth = 0
    def Height(Node):
        nonlocal LongestDepth
        if Node == None:
            return 0
        LH = Height(Node.left)
        RH = Height(Node.right)
        LongestDepth = max(LongestDepth,LH+RH)
        return 1+max(LH,RH)
    Height(Node)
    return LongestDepth

diameter = diameter(drinks)
print(f"The diameter of the Binary tree is : {diameter}\n-------------------------------------------")

# Check if the Binary tree is balanced or not 

def checkBalance(Node):
    if Node==None:
        return 0
    LH = checkBalance(Node.left)
    if LH == -1:
        return -1
    RH = checkBalance(Node.right)
    if RH == -1:
        return -1
    balance = abs(LH-RH)
    if balance>1:
        return -1

    return 1+max(LH,RH)

balanced = checkBalance(drinks)
if balanced == -1:
    print(f"The Binary Tree is not Balanced")
else:
    print(f"The Binary Tree is Balanced")