class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = SinglyLinkedList()

while True:
    print("\n1.Insert 2.Delete 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        ll.insert_end(int(input("Enter value: ")))
    elif choice == 2:
        ll.delete(int(input("Enter value to delete: ")))
    elif choice == 3:
        ll.display()
    else:
        break
