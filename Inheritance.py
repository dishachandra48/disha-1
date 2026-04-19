# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object
d = Dog()

# Access methods
d.speak()   # Inherited method
d.bark()    # Own method
