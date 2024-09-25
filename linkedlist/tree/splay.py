#Python Code for Search Operation of splay Trees
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
def newNode(data):
    newNode = Node(data)
    newNode.leftChild = newNode.rightChild = None
    return newNode
def rightRotate(x):
    y = x.leftChild
    x.leftChild = y.rightChild
    y.rightChild = x
    return y
def leftRotate(x):
    y = x.rightChild
    x.rightChild = y.leftChild
    y.leftChild = x
    return y
def splay(root, data):
    if root is None or root.data == data:
        return root
    if root.data > data:
        if root.leftChild is None:
            return root
        if root.leftChild.data > data:
            root.leftChild.leftChild = splay(root.leftChild.leftChild, data)
            root = rightRotate(root)
        elif root.leftChild.data < data:
            root.leftChild.rightChild = splay(root.leftChild.rightChild, data)
            if root.leftChild.rightChild is not None:
                root.leftChild = leftRotate(root.leftChild)   
        return root if root.leftChild is None else rightRotate(root)
    else:
        if root.rightChild is None:
            return root
        if root.rightChild.data > data:
            root.rightChild.leftChild = splay(root.rightChild.leftChild, data)
            if root.rightChild.leftChild is not None:
                root.rightChild = rightRotate(root.rightChild)
        elif root.rightChild.data < data:
            root.rightChild.rightChild = splay(root.rightChild.rightChild, data)
            root = leftRotate(root)
        return root if root.rightChild is None else leftRotate(root)
def insert(root, k):
    if root is None:
        return newNode(k) 
    root = splay(root, k)
    if root.data == k:
        return root
    newnode = newNode(k)
    if root.data > k:
        newnode.rightChild = root
        newnode.leftChild = root.leftChild
        root.leftChild = None
    else:
        newnode.leftChild = root
        newnode.rightChild = root.rightChild
        root.rightChild = None
    return newnode
def search(root, data):
    return splay(root, data)
def printTree(root):
    if root is None:
        return 
    if root is not None:
        printTree(root.leftChild)
        print(root.data, end=" ")
        printTree(root.rightChild)
def preOrder(root):
    if root != None:
        print(root.data, end = " ")
        preOrder(root.leftChild)
        preOrder(root.rightChild)
root = newNode(34)
root.leftChild = newNode(15)
root.rightChild = newNode(40)
root.leftChild.leftChild = newNode(12)
root.leftChild.leftChild.rightChild = newNode(14)
root.rightChild.rightChild = newNode(59)
print("The Splay tree is")
printTree(root)
ele = 34
print("\nElement to be searched ",ele)
root = search(root, ele)
print("Modified preorder traversal if element is found: ")
preOrder(root)