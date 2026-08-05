class Dog:
    def make_sound(self):
        return "Woof! Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Duck:
    def make_sound(self):
        return "Quack!"


# A uniform function that demonstrates polymorphism
def animal_speak(animal):
    # Calls the same method name, but behavior changes based on object type
    print(animal.make_sound())


# Create instances
animals = [Dog(), Cat(), Duck()]

# Loop through and call the method
for animal in animals:
    animal_speak(animal)