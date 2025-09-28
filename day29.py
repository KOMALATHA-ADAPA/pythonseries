# Day 29: Stack Implementation using List and linked list
#stack using list
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

# Pop element
print("Popped element:", stack.pop())
print("Stack after pop:", stack)

# Peek (top element)
print("Top element:", stack[-1])

# Check if empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

#stack using linked list
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None

    # Push element
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop element
    def pop(self):
        if self.top is None:
            return "Stack Underflow"
        popped = self.top.data
        self.top = self.top.next
        return popped

    # Peek (top element)
    def peek(self):
        if self.top is None:
            return "Empty Stack"
        return self.top.data

    # Display stack
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Testing ---
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack elements:")
s.display()

print("Top element:", s.peek())
print("Popped:", s.pop())
s.display()
