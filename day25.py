# Day 25: Singly Linked List Implementation

# Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.next = None      # Pointer to next node (initially None)

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node)

    # Method to add new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:          # If list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:           # Traverse to the last node
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Testing the Linked List ---
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked List:")
ll.display()
