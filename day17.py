# Day 19: File Handling in Python

#  Step 1: Writing to a file
# 'w' mode = write mode. It creates the file if it doesn't exist. Overwrites if it does.
with open("diary.txt", "w") as file:
    file.write("Dear Diary,\n")
    file.write("Today I learned how to handle files using Python!\n")

print(" File written successfully.")

#  Step 2: Appending to the same file
# 'a' mode = append mode. It adds content to the end of the file without deleting old data.
with open("diary.txt", "a") as file:
    file.write("I also practiced reading and writing files.\n")

print(" Content appended successfully.")

#  Step 3: Reading from the file
# 'r' mode = read mode. Reads the content of the file.
with open("diary.txt", "r") as file:
    content = file.read()

print("\n File Contents:")
print(content)

#  Step 4: Reading line by line
with open("diary.txt", "r") as file:
    print("\n Reading line by line:")
    for line in file:
        print(line.strip())  # .strip() removes the newline character at the end

#  Step 5: Checking if a file exists before reading
import os

if os.path.exists("diary.txt"):
    print("\n File exists, safe to read.")
else:
    print(" File does not exist!")

#  Step 6: Using try-except to handle file errors
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\n Error: File not found. Please check the filename.")
