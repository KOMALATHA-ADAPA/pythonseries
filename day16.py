# Basic try-except block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Execution completed.")

# Catching generic exception
try:
    data = [1, 2, 3]
    print(data[5])  # IndexError
except Exception as e:
    print("An error occurred:", e)

# Using else with try-except
try:
    x = 5
    y = 2
    print("Division:", x / y)
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("No error occurred!")

# Raising your own exception
age = -1
if age < 0:
    raise ValueError("Age cannot be negative")
