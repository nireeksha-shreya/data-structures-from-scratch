MAX = 5
queue = []

def enqueue(val):
    if len(queue) == MAX:
        print("Queue Overflow")
    else:
        queue.append(val)

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        print("Dequeued:", queue.pop(0))

def display():
    print(queue)

while True:
    print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue(int(input("Enter value: ")))
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    else:
        break
