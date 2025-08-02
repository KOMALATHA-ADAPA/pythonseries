# A dictionary stores data in key-value pairs
student = {
    "name": "Komalatha",
    "age": 22,
    "course": "Python",
    "marks": 90
}

# Printing the dictionary
print("Student Dictionary:", student)

# Accessing values using keys
print("Name:", student["name"])
print("Marks:", student.get("marks"))  # Using get() (returns None if key doesn't exist)

# Adding a new key-value pair
student["email"] = "komalatha@example.com"
print("After adding email:", student)

# Updating an existing value
student["marks"] = 95
print("After updating marks:", student)

# Deleting a key-value pair
del student["age"]
print("After deleting age:", student)

# Iterating over dictionary keys
print("All keys:")
for key in student:
    print(key)

# Iterating over key-value pairs
print("All key-value pairs:")
for key, value in student.items():
    print(f"{key} : {value}")

# Checking if a key exists
if "course" in student:
    print("Course exists!")

# Dictionary length
print("Total entries:", len(student))

# Nested dictionary
students = {
    "student1": {"name": "Komalatha", "marks": 90},
    "student2": {"name": "Anjali", "marks": 88}
}
print("Nested dictionary:", students)
print("Student2's name:", students["student2"]["name"])
