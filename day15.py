# Implicit Type Conversion (done automatically by Python)
x = 10      # int
y = 2.5     # float
z = x + y   # int + float => float
print("Implicit Conversion Result:", z)
print("Type of z:", type(z))  # Output: <class 'float'>

# Explicit Type Conversion (also called type casting)
# int() -> converts to integer
# float() -> converts to float
# str() -> converts to string
# list(), tuple(), set() etc. for containers

# String to int
num_str = "100"
num_int = int(num_str)
print("Converted to int:", num_int, type(num_int))

# Int to float
num_float = float(num_int)
print("Converted to float:", num_float)

# Float to int (decimal part is removed)
print("Float to int:", int(3.99))  # Output: 3

# Int to string
age = 22
age_str = str(age)
print("My age is " + age_str)

# List to set
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print("Converted to set:", my_set)

# Set to list
print("Set to list:", list(my_set))
