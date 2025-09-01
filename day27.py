# Day 27: Searching in a Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Append node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Search for a value in the list
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return f"Element {key} found at position {position}"
            current = current.next
            position += 1
        return f"Element {key} not found in the list"

    # Display linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Testing ---
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked List:")
ll.display()

print("\nSearching for 30:")
print(ll.search(30))

print("\nSearching for 50:")
print(ll.search(50))
