#  Day 6: Conditional Statements in Python

#  Conditional statements help us make decisions in our code based on conditions.
# Python uses keywords like if, elif, and else to control the flow.

# to work with conditional statements or a block of code we need to know about indentation
'''
Indentation refers to the spaces at the beginning of a line of code. Unlike many other programming languages, Python uses indentation to define blocks of code, especially for loops, conditionals, functions, and classes.
'''
# Correct indentation
if True:
    print("This is inside the if block")
print("This is outside the if block")
'''
Incorrect indentation (will throw an error)
if True:
print("This will cause an error")  #  IndentationError
'''
#  Basic if statement
# Executes the indented block only if the condition is True.
age = 18
if age >= 18:
    print("You are eligible to vote!")  # This line runs because the condition is True

#  if-else statement
# If the condition is True, the first block runs; otherwise, the else block runs.
marks = 45
if marks >= 50:
    print("You passed!")
else:
    print("You failed!")  # This will be printed because 45 < 50

#  if-elif-else ladder
# Used when you have multiple conditions to check.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")  # This gets executed because 85 ≥ 75 and < 90
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")

#  Nested if statements
# You can place one if statement inside another to check more specific conditions.
num = -3
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")  # This gets printed because num < 0

#  Taking input from user and using if-elif-else
# Demonstrates real-time decision making with input
temperature = int(input("Enter today's temperature: "))
if temperature > 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("It's a pleasant day.")
else:
    print("It's cold today.")

#  Best Practice: Always make sure your indentation is correct in Python.
# Blocks of code inside if, elif, else must be properly indented (usually 4 spaces).

