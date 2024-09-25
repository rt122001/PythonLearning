class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
class LL:
   def __init__(self):
      self.head = None
   def listprint(self):
      val = self.head
      print("Linked List:")
      while val is not None:
         print(val.data)
         val = val.next

l1 = LL()
l1.head = Node("23")
l2 = Node("12")
l3 = Node("7")
l4 = Node("14")
l5 = Node("61")

# Linking the first Node to second node
l1.head.next = l2

# Linking the second Node to third node
l2.next = l3
l3.next = l4
l4.next = l5
l1.listprint()