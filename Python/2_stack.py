stack = []

# PUSH in stack
def push():
    ele = input("Enter element: ")
    stack.append(ele)
    print(ele,"is pushed")

# POP in stack
def pop():
    if not stack:
        print("Stack is empty")
    else:
        x = stack.pop()
        print(x,"is popped")

# SHOW stack
def show():
    if not stack:
        print("Stack is empty")
    else:
        for i in reversed(stack):
            print(i)

# Menu
end = False
while not end:
    print("Menu:")
    print("1.PUSH")
    print("2.POP")
    print("3.SHOW")
    print("4. EXIT\n")
    
    c = int(input("Enter choice:"))
    
    if c == 1:
        push()
    elif c == 2:
        pop()
    elif c == 3:
        show()
    elif c == 4:
        end = True
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

