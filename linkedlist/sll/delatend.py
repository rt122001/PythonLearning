class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
 #Displaying the list
    def printList(self):
        p = self.head
        print("\n[", end="")
        while p != None:
            print(" " + str(p.data) + " ", end="")
            p = p.next
        print("]")
 #Insertion at the beginning
    def insertatbegin(self, data):
        #create a link
        lk = Node(data)
        #point it to old first node
        lk.next = self.head
        #point first to new first node
        self.head = lk

    def deleteatend(self):
        linkedlist = self.head
        while linkedlist.next.next != None:
            linkedlist = linkedlist.next
        linkedlist.next = None
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertatbegin(12)
    linked_list.insertatbegin(22)
    linked_list.insertatbegin(30)
    linked_list.insertatbegin(40)
    linked_list.insertatbegin(55)
    #print list
    print("Linked List: ", end="")
    linked_list.printList()
    linked_list.deleteatend()
    print("Linked List after deletion: ", end="")
    linked_list.printList()