class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
head = None
last = None
current = None
def isEmpty():
    return head == None
def printList():
    ptr = head
    while ptr != None:
        print(f"({ptr.key},{ptr.data})", end=" ")
        ptr = ptr.next
def insertFirst(key, data):
    global head, last
    link = Node(data, key)
    if isEmpty():
        last = link
    else:
        head.prev = link
    link.next = head
    head = link
def insertLast(key, data):
    global head, last
    link = Node(data, key)
    if isEmpty():
        last = link
    else:
        last.next = link
        link.prev = last
    last = link
insertFirst(1,10)
insertFirst(2,20)
insertFirst(3,30)
insertFirst(4,1)
insertLast(5,40)
insertLast(6,56)
print("Doubly Linked List: ", end="")
printList()