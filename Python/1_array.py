# an array
arr = []

# Inserting x in p position
def insert():
    ele = int(input("Enter element to insert: "))
    pos = int(input("Enter position to insert at: "))
    arr.insert(pos, ele)
    print(ele, "is inserted at position", pos)
    print(arr)

# Deleting p position
def delete():
    pos = int(input("Enter position to delete: "))
    if 0 <= pos < len(arr):
        print(arr[pos], "is deleted")
        del arr[pos]
        print(arr)
    else:
        print("Invalid position")

# Menu
end = False
while not end:
    print("Menu:")
    print("1. Insert")
    print("2. Delete")
    print("3. Show array")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert()
    elif choice == '2':
        delete()
    elif choice == '3':
        print("Array:", arr)
    elif choice == '4':
        end = True
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
