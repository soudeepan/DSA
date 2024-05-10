class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=", ")
            temp = temp.next
        print()

    def display_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=", ")
            temp = temp.prev
        print()

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def deleteNode(self, key):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        if self.head.data == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        while temp:
            if temp.data == key:
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp.prev.next = None
                return
            temp = temp.next

# Create a doubly linked list
dlist = DoublyLinkedList()

# Insert elements into the doubly linked list
dlist.insertAtBeginning(1)
dlist.insertAtEnd(2)
dlist.insertAtEnd(3)
dlist.insertAtEnd(4)

# Display the doubly linked list forward and backward
print("Doubly Linked List (Forward):")
dlist.display_forward()
print("\nDoubly Linked List (Backward):")
dlist.display_backward()

# Delete a node from the doubly linked list
print("\nDeleting node 2:")
dlist.deleteNode(2)
dlist.display_forward()
