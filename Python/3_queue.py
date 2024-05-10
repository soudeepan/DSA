from collections import deque

# Create an empty deque
deque = deque()

# Function to add an element to the front of the deque
def add_front():
    ele = input("Enter element to add to the front: ")
    deque.appendleft(ele)
    print(ele, "is added to the front.")
    print("Deque:", deque)

# Function to add an element to the rear of the deque
def add_rear():
    ele = input("Enter element to add to the rear: ")
    deque.append(ele)
    print(ele, "is added to the rear.")
    print("Deque:", deque)

# Function to remove an element from the front of the deque
def remove_front():
    if deque:
        ele = deque.popleft()
        print(ele, "is removed from the front.")
        print("Deque:", deque)
    else:
        print("Deque is empty.")

# Function to remove an element from the rear of the deque
def remove_rear():
    if deque:
        ele = deque.pop()
        print(ele, "is removed from the rear.")
        print("Deque:", deque)
    else:
        print("Deque is empty.")

# Function to display the deque
def display():
    if deque:
        print("Deque:", deque)
    else:
        print("Deque is empty.")

# Menu-driven interface
end = False
while not end:
    print("\nMenu:")
    print("1. Add to front")
    print("2. Add to rear")
    print("3. Remove from front")
    print("4. Remove from rear")
    print("5. Display deque")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_front()
    elif choice == '2':
        add_rear()
    elif choice == '3':
        remove_front()
    elif choice == '4':
        remove_rear()
    elif choice == '5':
        display()
    elif choice == '6':
        end = True
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
