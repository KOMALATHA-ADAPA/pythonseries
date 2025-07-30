# Defining strings
name = "Komalatha"
greeting = 'Hello, Python learners!'

# Printing strings
print(name)  # Output: Komalatha
print(greeting)  # Output: Hello, Python learners!

# String concatenation (joining two strings)
full_greeting = greeting + " I'm " + name
print(full_greeting)  # Output: Hello, Python learners! I'm Komalatha

# Accessing characters in a string (Indexing)
print(name[0])  # Output: K (1st character)
print(name[-1])  # Output: a (last character)

# Slicing strings
print(name[0:4])  # Output: Koma (from index 0 to 3)
print(name[2:])   # Output: malatha (from index 2 to end)
print(name[:5])   # Output: Komal (from start to index 4)

# String length
print(len(name))  # Output: 9

# String methods
print(name.upper())  # Output: KOMALATHA (converts to uppercase)
print(name.lower())  # Output: komalatha (converts to lowercase)
print(name.startswith("Ko"))  # Output: True
print(name.endswith("tha"))   # Output: True
print(name.replace("a", "@")) # Output: Kom@l@th@ (replaces all a's with @)

# Removing whitespace
str1 = "  Python  "
print(str1.strip())  # Output: Python

# Splitting a string into a list
sentence = "Python is fun"
print(sentence.split())  # Output: ['Python', 'is', 'fun']

# Joining a list of words into a string
words = ['Join', 'me', 'on', 'GitHub']
joined = ' '.join(words)
print(joined)  # Output: Join me on GitHub
