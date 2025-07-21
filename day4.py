# Day 4: Variables and Comments in Python

#  Single-line comment
# This program demonstrates variable creation, usage, and comments in Python

# Variable assignment
name = "Komalatha"      # string
age = 22                # integer
height = 5.4            # float
is_student = True       # boolean

#  Print formatted output using f-strings
print(f"My name is {name}, I am {age} years old and {height} feet tall.")
print(f"Am I a student? {is_student}")

#  Updating variables
age = 23  # age updated
print(f"Updated age: {age}")

#  Multi-line comment
"""
This is a multi-line comment.
Useful for longer descriptions or documentation.
The following section demonstrates different data types.
"""

#  Different data types
score = 85
grade = 'A'
is_passed = True
gpa = 9.2
college = None

#  Type checking
print(type(name))       # <class 'str'>
print(type(score))      # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(college))    # <class 'NoneType'>

#  Variable Swapping
x = 5
y = 10
print(f"Before swapping: x = {x}, y = {y}")
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")

#  Constant (by convention, written in all caps)
PI = 3.14159
print(f"The value of PI is: {PI}")

#  Naming rules and conventions
userName = "komalatha"
_user_id = 101
user2 = "PythonLearner"

#  Invalid variable names (uncommenting will cause error)
# 2user = "error"   # Cannot start with a number
# user-name = "no"  # Hyphens are not allowed
# if = "keyword"    # Cannot use keywords

#  Best practice: Use meaningful variable names
full_name = "Komalatha Adapa"
total_marks = 480
percentage = (total_marks / 500) * 100
print(f"{full_name} scored {percentage}%")

