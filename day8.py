# Day 8: while Loops in Python

# A while loop keeps executing a block of code as long as the given condition is True.

# Example 1: Basic while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop

# Explanation:
# The loop starts with count = 1 and keeps running until count becomes greater than 5.
# If we forget to increment, the loop will run forever (infinite loop).

print("-----")

# Example 2: Using break to exit a loop early
x = 1
while x < 10:
    print("x is", x)
    if x == 4:
        print("Breaking the loop at x =", x)
        break  # Exit the loop when x is 4
    x += 1

print("-----")

# Example 3: Using continue to skip an iteration
y = 0
while y < 5:
    y += 1
    if y == 3:
        print("Skipping value 3")
        continue  # Skip the rest of the loop for y = 3
    print("y =", y)

print("-----")

# Example 4: Using else with while loop
z = 0
while z < 3:
    print("z =", z)
    z += 1
else:
    print("Loop completed successfully!")  # This runs when while condition becomes False

# Note:
# The else block runs only if the while loop wasn't exited using break.

print("-----")

# Real-world example: Password attempts
# Allowing the user 3 attempts to enter correct password
correct_password = "komal123"
attempts = 0
while attempts < 3:
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Access granted ")
        break
    else:
        print("Incorrect password ")
        attempts += 1
else:
    print("Too many attempts! Access denied ")
