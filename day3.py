# Day 3: print() and input() functions
#---------------------------------------------------------------------------------------------------------#
'''
The print() function is used to display information on the screen. 
It's one of the most commonly used functions in Python and is essential for debugging, showing results, or interacting with users.'''
# Using print() to display text
print("Welcome to Day 3 of the Python series!")
print("Let's learn how to display and take input in Python.")
#----------------------------------------------------------------------------------------------------------#
'''The input() function is used to take input from the user.
 It pauses the program and waits for the user to type something, then returns it as a string.'''
# Taking user input
name = input("What is your name? ")
age = input("How old are you? ")

# Displaying formatted output
print("Hello " + name + "! You are " + age + " years old.")
print(f"Nice to meet you, {name}. You're {age} years young!")

# Another example: simple calculator
print("\nLet's try a basic calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
#----------------------------------------------------------------------------------------------------------#
print(f"The sum of {num1} and {num2} is {result}")
#\n → New line
#\t → Tab space
print("using new line here \n and now using : \t :tab space here")  # Prints on two lines
