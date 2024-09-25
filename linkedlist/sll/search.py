class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLL:
   def listprint(self):
      printval = self.head
      print("Linked List: ")
      while printval is not None:
         print (printval.data)
         printval = printval.next
   def __init__(self):
      self.head = None
   def search(self, x):
      count = 0
      
      # Initialize current to head
      current = self.head

      # loop till current not equal to None
      while current != None:
         if current.data == x:
            print("Element is found")
            count = count + 1
         current = current.next
      if count == 0:
         print("Element is not found in the list")

l1 = SLL()
l1.head = Node("731")
e2 = Node("672")
e3 = Node("63")

l1.head.next = e2
e2.next = e3
l1.listprint()
ele = "63"
print("Element to be searched is: ", ele);
l1.search(ele)