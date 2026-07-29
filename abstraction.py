from abc import ABC, abstractmethod


# Abstract Class (Template)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Hidden implementation detail


# Concrete Subclasses (Actual implementations)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Usage
pets = [Dog(), Cat()]

for pet in pets:
    print(pet.make_sound())  # Output: Woof! then Meow!

# Animal()  # TypeError: Cannot instantiate abstract class directly