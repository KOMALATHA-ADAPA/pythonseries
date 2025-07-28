# Day 9: Functions in Python 

# What is a function?
# A function is a block of reusable code that performs a specific task.
# Functions help organize your code and make it modular.

#  Defining a basic function using the 'def' keyword
def greet():
    # This function prints a greeting message
    print("Hello, welcome to Day 9 of Python series!")

# Calling the function
greet()

print("-----")

#  Function with parameters
def greet_user(name):
    # This function takes a name as input and prints a personalized greeting
    print(f"Hello {name}, have a great day learning Python!")

# Calling the function with different arguments
greet_user("Komalatha")
greet_user("Python Enthusiast")

print("-----")

#  Function with return value
def add(a, b):
    # This function adds two numbers and returns the result
    result = a + b
    return result

# Using the return value
sum_result = add(10, 15)
print("Sum is:", sum_result)

print("-----")

#  Function with default arguments
def greet_with_language(name, language="Python"):
    # If no language is passed, default will be Python
    print(f"{name} is learning {language}.")

greet_with_language("Komalatha")           # uses default
greet_with_language("Komalatha", "Java")   # uses passed argument

print("-----")

#  Function with multiple return values
def calculate(a, b):
    # Returns sum, difference, and product
    return a + b, a - b, a * b

# Receiving multiple return values
s, d, p = calculate(5, 3)
print(f"Sum: {s}, Difference: {d}, Product: {p}")

print("-----")

# Function with variable number of arguments using *args
def print_friends(*friends):
    print("My friends are:")
    for friend in friends:
        print(friend)

print_friends("Alice", "Bob", "Charlie")

print("-----")

#  Keyword arguments using **kwargs
def display_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

display_info(name="Komalatha", age=22, course="Python")

print("-----")

#  Lambda (anonymous) function
# Used for short, one-line functions
square = lambda x: x * x
print("Square of 6 is:", square(6))
