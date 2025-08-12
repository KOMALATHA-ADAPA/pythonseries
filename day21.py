"""
Day 21: Regular Expressions in Python
--------------------------------------
Regular Expressions (regex) allow us to search, match, and manipulate strings 
based on patterns.
We use the 're' module in Python for regex operations.
"""

import re  # Import the regular expressions module

# 1. Basic match using re.match()
pattern = r"Python"
text = "Python is amazing"
match = re.match(pattern, text)
if match:
    print("Match found using match():", match.group())  # group() returns matched text
else:
    print("No match found using match()")

# 2. Searching anywhere in the string using re.search()
pattern = r"amazing"
search_result = re.search(pattern, text)
if search_result:
    print("Search found:", search_result.group())
else:
    print("No search match found")

# 3. Finding all matches using re.findall()
sentence = "I have 2 apples and 5 bananas."
numbers = re.findall(r"\d+", sentence)  # \d+ means one or more digits
print("Numbers found:", numbers)

# 4. Replacing text using re.sub()
new_sentence = re.sub(r"bananas", "oranges", sentence)
print("After replacement:", new_sentence)

# 5. Splitting text using re.split()
split_text = re.split(r"\s+", sentence)  # \s+ means one or more spaces
print("Split text:", split_text)

# 6. Example: Validate email address
email = "test@example.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
    print("Valid email format")
else:
    print("Invalid email format")
