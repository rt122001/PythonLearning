class Node(object):
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1
class AVLTree(object):
   def insert(self, root, key):
      if not root:
         return Node(key)
      elif key < root.data:
         root.left = self.insert(root.left, key)
      else:
         root.right = self.insert(root.right, key)
      root.h = 1 + max(self.getHeight(root.left),
         self.getHeight(root.right))
      b = self.getBalance(root)
      if b > 1 and key < root.left.data:
         return self.rightRotate(root)
      if b < -1 and key > root.right.data:
         return self.leftRotate(root)
      if b > 1 and key > root.left.data:
         root.left = self.lefttRotate(root.left)
         return self.rightRotate(root)
      if b < -1 and key < root.right.data:
          root.right = self.rightRotate(root.right)
          return self.leftRotate(root)
      return root
   def delete(self, root, key):
      if not root:
         return root
      elif key < root.data:
         root.left = self.delete(root.left, key)
      elif key > root.data:
         root.right = self.delete(root.right, key)
      else:
         if root.left is None:
            temp = root.right
            root = None
            return temp
         elif root.right is None:
            temp = root.left
            root = None
            return temp
         temp = self.getMindataueNode(root.right)
         root.data = temp.data
         root.right = self.delete(root.right, temp.data)
      if root is None:
         return root
      root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
      balance = self.getBalance(root)
      if balance > 1 and self.getBalance(root.left) >= 0:
         return self.rightRotate(root)
      if balance < -1 and self.getBalance(root.right) <= 0:
         return self.leftRotate(root)
      if balance > 1 and self.getBalance(root.left) < 0:
         root.left = self.leftRotate(root.left)
         return self.rightRotate(root)
      if balance < -1 and self.getBalance(root.right) > 0:
         root.right = self.rightRotate(root.right)
         return self.leftRotate(root)
      return root
   def leftRotate(self, z):
      y = z.right
      T2 = y.left
      y.left = z
      z.right = T2
      z.height = 1 + max(self.getHeight(z.left),
         self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
         self.getHeight(y.right))
      return y
   def rightRotate(self, z):
      y = z.left
      T3 = y.right
      y.right = z
      z.left = T3
      z.height = 1 + max(self.getHeight(z.left),
         self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
         self.getHeight(y.right))
      return y
   def getHeight(self, root):
      if not root:
         return 0
      return root.height
   def getBalance(self, root):
      if not root:
         return 0
      return self.getHeight(root.left) - self.getHeight(root.right)
   def Inorder(self, root):
      if root.left:
         self.Inorder(root.left)
      print(root.data, end = " ")
      if root.right:
         self.Inorder(root.right)

Tree = AVLTree()
root = None
root = Tree.insert(root, 10)
root = Tree.insert(root, 13)
root = Tree.insert(root, 11)
root = Tree.insert(root, 14)
root = Tree.insert(root, 12)
root = Tree.insert(root, 15)

# Inorder Traversal
print("AVL Tree: ")
Tree.Inorder(root)
root = Tree.delete(root, 14)
print("\nAfter deletion: ")
Tree.Inorder(root)