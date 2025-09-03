# Day 28: Doubly Linked List Implementation

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to last node
            last = last.next
        last.next = new_node
        new_node.prev = last  # Link back to previous node

    # Display list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            last = current
            current = current.next
        print("None")

    # Display list backward
    def display_backward(self):
        current = self.head
        # Go to the last node
        while current and current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# --- Testing ---
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Doubly Linked List (Forward):")
dll.display_forward()

print("\nDoubly Linked List (Backward):")
dll.display_backward()
