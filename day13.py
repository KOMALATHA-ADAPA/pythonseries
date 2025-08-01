# Creating a set
fruits = {"apple", "banana", "cherry", "banana"}  # Duplicates are ignored
print("Fruits set:", fruits)

# Adding elements
fruits.add("mango")
print("After adding mango:", fruits)

# Adding multiple elements
fruits.update(["grape", "kiwi"])
print("After update:", fruits)

# Removing elements
fruits.remove("banana")  # Removes 'banana'; throws error if not found
print("After removing banana:", fruits)

fruits.discard("apple")  # Discards 'apple'; does NOT throw error if not found
print("After discarding apple:", fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))          # All unique elements
print("Intersection:", set1.intersection(set2))  # Common elements
print("Difference:", set1.difference(set2))      # Items only in set1
print("Symmetric Difference:", set1.symmetric_difference(set2))  # In either, but not both

# Membership test
print("Is 3 in set1?", 3 in set1)

# Looping through a set
for item in fruits:
    print("Fruit:", item)

# Length of set
print("Total fruits:", len(fruits))
