# Day 10: Python Lists 

#  What is a list?
# A list is an ordered, mutable collection of items. You can store different data types in a list.

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

#  Accessing elements (indexing starts from 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative indexing

#  Changing list elements
fruits[1] = "blueberry"
print("Updated Fruits List:", fruits)

#  List length
print("Number of fruits:", len(fruits))

#  Adding elements
fruits.append("orange")         # Adds at the end
fruits.insert(1, "grape")       # Adds at a specific index
print("After Adding Elements:", fruits)

#  Removing elements
fruits.remove("apple")          # Removes by value
popped = fruits.pop()           # Removes last element and returns it
print("After Removal:", fruits)
print("Popped item:", popped)

#  Looping through a list
print("All Fruits:")
for fruit in fruits:
    print(fruit)

#  Checking if an item exists
if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

#  List slicing
numbers = [10, 20, 30, 40, 50, 60]
print("First three numbers:", numbers[:3])  # Slices first 3 items
print("Last two numbers:", numbers[-2:])    # Last two items

#  Sorting a list
numbers.sort()     # Sorts in ascending order
print("Sorted numbers:", numbers)

numbers.reverse()  # Reverses the list
print("Reversed numbers:", numbers)

#  Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix:")
for row in matrix:
    print(row)
