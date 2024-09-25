class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # display the list
    def printList(self):
        p = self.head
        print("\n[", end="")
        #start from the beginning
        while(p != None):
            print(" ", p.data, " ", end="")
            p = p.next
        print("]")
    #insertion at the beginning
    def insertatbegin(self, data):
        #create a link
        lk = Node(data)
        # point it to old first node
        lk.next = self.head
        #point first to new first node
        self.head = lk
    def deletenode(self, key):
        temp = self.head
        if (temp != None and temp.data == key):
            self.head = temp.next
            return
        # Find the key to be deleted
        while (temp != None and temp.data != key):
            prev = temp
            temp = temp.next
        # If the key is not present
        if (temp == None):
            return
        # Remove the node
        prev.next = temp.next
llist = LinkedList()
llist.insertatbegin(12)
llist.insertatbegin(22)
llist.insertatbegin(30)
llist.insertatbegin(40)
llist.insertatbegin(55)
print("Original Linked List: ", end="")
# print list
llist.printList()
llist.deletenode(30)
print("Linked List after deletion: ", end="")
# print list
llist.printList()