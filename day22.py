# Day 22: List Comprehension & Lambda Functions in Python

# ------------------------
# PART 1: LIST COMPREHENSION
# ------------------------
# List comprehension is a short and efficient way to create lists from an existing iterable.

# Example 1: Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Get even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", evens)  # Output: [2, 4, 6, 8, 10]

# Example 3: Convert list of words to uppercase
words = ["python", "is", "fun"]
uppercase_words = [word.upper() for word in words]
print("Uppercase Words:", uppercase_words)  # Output: ['PYTHON', 'IS', 'FUN']

# ------------------------
# PART 2: LAMBDA FUNCTIONS
# ------------------------
# Lambda functions are small, anonymous functions created with the 'lambda' keyword.

# Example 1: Lambda to add two numbers
add = lambda a, b: a + b
print("Addition:", add(5, 3))  # Output: 8

# Example 2: Lambda to find square of a number
square = lambda x: x**2
print("Square of 4:", square(4))  # Output: 16

# Example 3: Using lambda with 'map' to double a list of numbers
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print("Doubled Numbers:", doubled)  # Output: [2, 4, 6, 8, 10]

# Example 4: Using lambda with 'filter' to get odd numbers
odds = list(filter(lambda x: x % 2 != 0, nums))
print("Odd Numbers:", odds)  # Output: [1, 3, 5]

# ------------------------
# COMBINING LIST COMPREHENSION + LAMBDA
# ------------------------
# Example: Square only even numbers from the list
even_squares = [square(x) for x in nums if x % 2 == 0]
print("Even Squares:", even_squares)  # Output: [4, 16]
