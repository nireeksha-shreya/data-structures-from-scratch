MAX = 5
stack = []

def push(val):
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        stack.append(val)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Popped:", stack.pop())

def display():
    print(stack)

while True:
    print("\n1.Push 2.Pop 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        push(int(input("Enter value: ")))
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    else:
        break
