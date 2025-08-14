# Day 23: The math Module in Python
# The math module gives us access to many useful mathematical functions and constants.

import math  # Import the math module

# 1. Mathematical Constants
print("Pi value:", math.pi)  # 3.141592653589793
print("Euler's number (e):", math.e)  # 2.718281828459045

# 2. Square Root
# math.sqrt(x) returns the square root of x
print("\nSquare root of 16:", math.sqrt(16))  # 4.0

# 3. Power
# math.pow(x, y) returns x raised to the power of y
print("2 raised to power 3:", math.pow(2, 3))  # 8.0

# 4. Factorial
# math.factorial(n) returns n!
print("Factorial of 5:", math.factorial(5))  # 120

# 5. Rounding
# math.floor(x) → rounds down to nearest integer
# math.ceil(x) → rounds up to nearest integer
print("\nFloor of 4.9:", math.floor(4.9))  # 4
print("Ceil of 4.1:", math.ceil(4.1))  # 5

# 6. Trigonometric Functions
# math.sin(), math.cos(), math.tan() take angles in radians
print("\nSine of 90 degrees:", math.sin(math.radians(90)))  # 1.0
print("Cosine of 0 degrees:", math.cos(math.radians(0)))  # 1.0
print("Tangent of 45 degrees:", math.tan(math.radians(45)))  # 1.0

# 7. Degree & Radian Conversion
# math.radians(x) → converts degrees to radians
# math.degrees(x) → converts radians to degrees
print("\n180 degrees in radians:", math.radians(180))  # 3.141592653589793
print("π radians in degrees:", math.degrees(math.pi))  # 180.0

# 8. Logarithmic Functions
# math.log(x) → natural log (base e)
# math.log10(x) → log base 10
print("\nNatural log of e:", math.log(math.e))  # 1.0
print("Log base 10 of 1000:", math.log10(1000))  # 3.0

# 9. GCD (Greatest Common Divisor)
print("\nGCD of 48 and 60:", math.gcd(48, 60))  # 12

# Summary:
# - Use math module for advanced calculations
# - Provides constants, trigonometry, logarithms, rounding, factorials, and more

print("\nMath module makes Python a powerful tool for mathematics and engineering!")
