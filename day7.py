# Day 7: Python Loops - for loop
# --------------------------------------
# In Python, a for loop is used to iterate over a sequence (such as a list, tuple, dictionary, string, or range).
# This allows you to execute a block of code multiple times, once for each item in the sequence.

# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # 'fruit' is the loop variable; each value from the list is assigned to it one by one
    print(fruit)

print("----------")

# Example 2: Iterating through a string
# Strings are also iterable, so we can loop through each character
for letter in "Python":
    print(letter)

print("----------")

# Example 3: Using the range() function
# range(start, stop) generates a sequence of numbers from 'start' to 'stop-1'
for i in range(1, 6):  # 1 to 5
    print(i)

print("----------")

# Example 4: Using range() with step
# range(start, stop, step) allows us to skip numbers in the sequence
for i in range(0, 10, 2):  # Even numbers from 0 to 8
    print(i)

print("----------")

# Example 5: Nested for loop
# You can place one loop inside another for more complex iterations
for i in range(1, 3):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")

print("----------")

# Example 6: Using 'break' to exit the loop early
for num in range(1, 10):
    if num == 5:
        break  # loop stops when num becomes 5
    print(num)

print("----------")

# Example 7: Using 'continue' to skip an iteration
for num in range(1, 6):
    if num == 3:
        continue  # skip printing 3
    print(num)

print("----------")

# Example 8: for loop with else
# The 'else' block is executed only if the loop completes normally (not terminated by break)
for num in range(1, 4):
    print(num)
else:
    print("Loop finished without break.")

print("----------")

# Example 9: for loop over a tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

print("----------")

# Example 10: for loop over a dictionary
# Iterating through dictionary keys and values
student = {"name": "Komalatha", "age": 22, "branch": "IT"}
for key in student:
    print(f"{key} => {student[key]}")
