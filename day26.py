# Day 26: Linked List - Insertion & Deletion

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

    # Insert node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to old head
        self.head = new_node       # Move head to new node

    # Delete node by value
    def delete_node(self, key):
        temp = self.head

        # If head itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    # Display linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Testing ---
ll = LinkedList()
ll.append(20)
ll.append(30)
ll.append(40)

print("Original List:")
ll.display()

ll.insert_at_beginning(10)
print("\nAfter inserting 10 at beginning:")
ll.display()

ll.delete_node(30)
print("\nAfter deleting 30:")
ll.display()
