#Python code for doubly linked list
class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
#this link always point to first Link
head = None
#this link always point to last Link
last = None
current = None
#is list empty
def isEmpty():
    return head == None
#display the doubly linked list
def printList():
    ptr = head
    while ptr != None:
        print(f"({ptr.key},{ptr.data}) ", end="")
        ptr = ptr.next
#insert link at the first location
def insertFirst(key, data):
    #create a link
    global head, last
    link = Node(data, key)
    if isEmpty():
        #make it the last link
        last = link
    else:
        #update first prev link
        head.prev = link
    #point it to old first link
    link.next = head
    head = link
#delete first item
def deleteFirst():
     #save reference to first link
    global head, last
    tempLink = head
    #if only one link
    if head.next == None:
        last = None
    else:
        head.next.prev = None
    head = head.next
    #return the deleted link
    return tempLink
insertFirst(1,10)
insertFirst(2,20)
insertFirst(3,30)
insertFirst(4,1)
insertFirst(5,40)
insertFirst(6,56)
print("Doubly Linked List:")
printList()
print("\nList after deleting first record:")
deleteFirst()
printList()