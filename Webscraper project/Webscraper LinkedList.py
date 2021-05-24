data = [1.25, 1.78, 1.2156115]

class Node:
     def __init__(self, data, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

# insertion method for the linked list
def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

# print method for the linked list
def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

first = Node(data)
print(first.data)
# Singly Linked List with insertion and print methods
#LL = LinkedList()
#LL.insert(3)
#LL.insert(4)
#LL.insert(5)
#LL.printLL()