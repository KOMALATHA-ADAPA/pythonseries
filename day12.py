# Creating a tuple
my_tuple = ("apple", "banana", "cherry")
print("Original tuple:", my_tuple)

# Accessing elements by index
print("First fruit:", my_tuple[0])

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)
print("Mixed tuple:", mixed_tuple)

# Nested tuple
nested = ("Komalatha", [1, 2, 3], (4, 5))
print("Nested tuple:", nested)

# Tuples are immutable, the following line would cause an error:
# my_tuple[1] = "orange"

# But if the tuple contains mutable elements (like a list), those can be changed
nested[1].append(4)
print("After modifying the list inside tuple:", nested)

# Tuple unpacking
person = ("Komalatha", 22, "India")
name, age, country = person
print(f"My name is {name}, I am {age} years old, from {country}")

# Tuple functions
numbers = (5, 3, 8, 5)
print("Count of 5:", numbers.count(5))  # Counts how many times 5 appears
print("Index of 8:", numbers.index(8))  # Finds the index of 8
