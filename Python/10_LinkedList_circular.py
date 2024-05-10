class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=",")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node  # Circular reference to itself
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node  # Circular reference to itself
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def deleteNode(self, key):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        # If head is the only node in the list
        if self.head.data == key and self.head.next == self.head:
            self.head = None
            return

        # If head needs to be removed
        if self.head.data == key:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            temp = self.head
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == key:
                    prev.next = temp.next
                    temp = temp.next
            if temp.data == key:
                prev.next = self.head

# Create a circular linked list
clist = CircularLinkedList()

# Insert elements into the circular linked list
clist.insertAtBeginning(1)
clist.insertAtEnd(2)
clist.insertAtEnd(3)
clist.insertAtEnd(4)

# Display the circular linked list
print("Circular Linked List:")
clist.display()

# Delete a node from the circular linked list
print("\nDeleting node 2:")
clist.deleteNode(2)
clist.display()
