#python program for circular linked list
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
head = None
current = None
def is_empty():
    return head is None
#insert link at the first location
def insert_first(key, data):
    #create a link
    global head
    new_node = Node(key, data)
    if is_empty():
        head = new_node
        head.next = head
    else:
        #point it to old first node
        new_node.next = head
        #point first to the new first node
        head = new_node
        
def print_list():
    global head
    ptr = head
    print("[", end=" ")
    #start from the beginning
    if head is not None:
        while ptr.next != ptr:
            print("({}, {})".format(ptr.key, ptr.data), end=" ")
            ptr = ptr.next
        print("]")
def delete_first():
    global head
    temp_link = head
    if head.next == head:
        head = None
        return temp_link
    head = head.next
    return temp_link  
insert_first(1, 10)
insert_first(2, 20)
insert_first(3, 30)
insert_first(4, 1)
insert_first(5, 40)
insert_first(6, 56)
#printlist
print("Circular Linked List: ")
print_list()
delete_first()
print("\nList after deleting the first item: ")
print_list();