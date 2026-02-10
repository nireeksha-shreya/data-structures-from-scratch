def insert(arr, pos, val):
    arr.insert(pos, val)

def delete(arr, pos):
    if pos < len(arr):
        arr.pop(pos)

def search(arr, val):
    if val in arr:
        return arr.index(val)
    return -1

def display(arr):
    print(arr)

arr = list(map(int, input("Enter elements: ").split()))

while True:
    print("\n1.Insert 2.Delete 3.Search 4.Display 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        pos, val = map(int, input("Enter position and value: ").split())
        insert(arr, pos, val)

    elif choice == 2:
        pos = int(input("Enter position to delete: "))
        delete(arr, pos)

    elif choice == 3:
        val = int(input("Enter value to search: "))
        res = search(arr, val)
        print("Found at index" if res != -1 else "Not found", res)

    elif choice == 4:
        display(arr)

    else:
        break
