# 1. Global Variable
domain = "Animals"


class Cat:
    # 2. Class Variable
    species = "Felis catus"

    def __init__(self, name):
        # 3. Instance Variable
        self.name = name

    def sound(self, loudness):
        # 4. Local Variable
        msg = f"{self.name} meows at volume {loudness}!"
        return msg


# Usage
cat = Cat("Whiskers")

print(domain)           # Global: Animals
print(Cat.species)      # Class: Felis catus
print(cat.name)         # Instance: Whiskers
print(cat.sound(5))     # Local (msg): Whiskers meows at volume 5!