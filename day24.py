# Day 24: Word Frequency Counter
# Let's solve this problem using Python series concepts

import string             # Import string module to access string constants like punctuation
from collections import Counter  # Import Counter class to count occurrences of items easily

# Take paragraph input from user
text = input("Enter a paragraph: ")

# Convert text to lowercase
text = text.lower()  # str.lower() converts all characters in the string to lowercase

# Remove punctuation
text = text.translate(
    str.maketrans('', '', string.punctuation)
)
# str.maketrans('', '', string.punctuation) creates a translation table that deletes all punctuation
# str.translate(...) applies the translation table to remove punctuation from the string

# Split text into words
words = text.split()  # str.split() splits the string into a list of words based on spaces

# Count frequency of each word
word_counts = Counter(words)  
# Counter(words) counts how many times each element appears in the list and stores it as a dictionary-like object

# Get the top 3 most frequent words
top_words = word_counts.most_common(3)  
# most_common(3) returns a list of the 3 most common elements as (element, count) tuples

# Print the results
print("\nTop 3 most frequent words:")
for word, count in top_words:
    print(f"{word}: {count}")  
    # f-string (formatted string) prints word and its frequency in a readable format
