# Queue implementation using collections.deque
from collections import deque

queue = deque()

# Enqueue operation
def enqueue():
    ele = input("Enter element to enqueue: ")
    queue.append(ele)
    print(ele, "is enqueued.")
    print("Queue:", queue)

# Dequeue operation
def dequeue():
    if queue:
        ele = queue.popleft()
        print(ele, "is dequeued.")
        print("Queue:", queue)
    else:
        print("Queue is empty.")

# Display queue
def display():
    if queue:
        print("Queue:", queue)
    else:
        print("Queue is empty.")

# Menu
end = False
while not end:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        end = True
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
