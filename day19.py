# Day 19: Polymorphism in Python
# --------------------------------
# Polymorphism means "many forms".
# In Python, it allows us to use the same method name for different types of objects.
# The method will behave differently depending on the object that is calling it.

# --------------------------
# Example 1: Polymorphism with functions
# --------------------------

def add(a, b, c=0):
    """
    Function to add numbers.
    The same function name 'add' works with 2 or 3 arguments.
    """
    return a + b + c

print(add(2, 3))          # Works with 2 arguments
print(add(2, 3, 4))       # Works with 3 arguments


# --------------------------
# Example 2: Polymorphism with class methods
# --------------------------

class Dog:
    def sound(self):
        return "Bark 🐶"

class Cat:
    def sound(self):
        return "Meow 🐱"

class Cow:
    def sound(self):
        return "Moo 🐄"

# A common interface
def make_sound(animal):
    """
    This function accepts any object that has a 'sound' method.
    It doesn't care what the actual type of object is.
    """
    print(animal.sound())

# Calling the same function for different objects
dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)  # Bark
make_sound(cat)  # Meow
make_sound(cow)  # Moo


# --------------------------
# Example 3: Polymorphism with Inheritance
# --------------------------

class Bird:
    def intro(self):
        print("I am a bird.")

    def flight(self):
        print("Some birds can fly, some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("I can fly high in the sky.")

class Ostrich(Bird):
    def flight(self):
        print("I cannot fly.")

bird1 = Sparrow()
bird2 = Ostrich()

for bird in (bird1, bird2):
    bird.intro()   # Same method from parent
    bird.flight()  # Different behavior for each child

"""
📌 Key Notes:
1. Polymorphism helps write generic, reusable code.
2. The same function or method name can be used for different types of objects.
3. Common in frameworks and large-scale projects for flexibility.
"""
