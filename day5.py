# Day 5: Operators in Python
# This script demonstrates various types of operators used in Python.

#  Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}")     # Addition
print(f"a - b = {a - b}")     # Subtraction
print(f"a * b = {a * b}")     # Multiplication
print(f"a / b = {a / b}")     # Division (returns float)
print(f"a // b = {a // b}")   # Floor Division (returns integer)
print(f"a % b = {a % b}")     # Modulus (remainder)
print(f"a ** b = {a ** b}")   # Exponentiation (power)

print("\n")

#  Comparison (Relational) Operators
print("Comparison Operators:")
print(f"a == b: {a == b}")    # Equal to
print(f"a != b: {a != b}")    # Not equal to
print(f"a > b: {a > b}")      # Greater than
print(f"a < b: {a < b}")      # Less than
print(f"a >= b: {a >= b}")    # Greater than or equal to
print(f"a <= b: {a <= b}")    # Less than or equal to

print("\n")

#  Assignment Operators
x = 5
print("Assignment Operators:")
x += 3   # Equivalent to x = x + 3
print(f"x += 3: {x}")
x -= 2   # Equivalent to x = x - 2
print(f"x -= 2: {x}")
x *= 4   # Equivalent to x = x * 4
print(f"x *= 4: {x}")
x /= 3   # Equivalent to x = x / 3
print(f"x /= 3: {x}")

print("\n")

#  Logical Operators
p = True
q = False
print("Logical Operators:")
print(f"p and q: {p and q}")   # True if both are True
print(f"p or q: {p or q}")     # True if at least one is True
print(f"not p: {not p}")       # True if p is False

print("\n")

#  Bitwise Operators (operate on binary numbers)
m = 6  # 110
n = 3  # 011
print("Bitwise Operators:")
print(f"m & n: {m & n}")       # Bitwise AND: 110 & 011 = 010 (2)
print(f"m | n: {m | n}")       # Bitwise OR:  110 | 011 = 111 (7)
print(f"m ^ n: {m ^ n}")       # Bitwise XOR: 110 ^ 011 = 101 (5)
print(f"~m: {~m}")             # Bitwise NOT: ~110 = -7
print(f"m << 1: {m << 1}")     # Left shift:  110 << 1 = 1100 (12)
print(f"m >> 1: {m >> 1}")     # Right shift: 110 >> 1 = 011 (3)

print("\n")

#  Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Identity Operators:")
print(f"a is b: {a is b}")         # True, both point to same object
print(f"a is c: {a is c}")         # False, different objects with same content
print(f"a is not c: {a is not c}") # True

print("\n")

#  Membership Operators
fruits = ["apple", "banana", "cherry"]
print("Membership Operators:")
print(f"'banana' in fruits: {'banana' in fruits}")   # True
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True
