class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
class SLL:
   def __init__(self):
      self.head = None

# Print the linked list
   def listprint(self):
      printval = self.head
      print("Linked List: ")
      while printval is not None:
         print (printval.data)
         printval = printval.next
   def AddAtBeginning(self,newdata):
      NewNode = Node(newdata)

      # Update the new nodes next val to existing node
      NewNode.next = self.head
      self.head = NewNode

l1 = SLL()
l1.head = Node("731")
e2 = Node("672")
e3 = Node("63")

l1.head.next = e2
e2.next = e3

l1.listprint()
l1.AddAtBeginning("122")
l1.listprint()