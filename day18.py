# Parent class (Base)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        # Method overriding
        print(f"{self.name} barks.")

# Another Child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Multilevel Inheritance
class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing with a ball.")

# Hierarchical Example
dog1 = Dog("Rocky")
cat1 = Cat("Whiskers")
puppy1 = Puppy("Tommy")

# Demonstrate polymorphism (same method name, different behavior)
dog1.speak()     # Rocky barks.
cat1.speak()     # Whiskers meows.
puppy1.speak()   # Tommy barks (inherits from Dog)
puppy1.play()    # Tommy is playing with a ball.
