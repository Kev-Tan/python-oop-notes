# This is based on Clear Code's tutorial on OOP
# Notes was written by myself, and then formatted using ChatGPT

# ============================================================
# Python Dunder (Magic) Methods — Learning Notes
# ============================================================
# Dunder methods are special methods in Python that are
# automatically called when certain built-in operations occur.
#
# Examples:
#   __init__  -> object creation
#   __len__   -> len(object)
#   __str__   -> print(object)
#   __add__   -> object + other
#   __call__  -> object()
# ============================================================


class Monster:
    """
    Monster class to demonstrate common dunder methods.
    """

    # --------------------------------------------------------
    # __init__ (Constructor)
    # --------------------------------------------------------
    # Called automatically when an object is created.
    # Used to initialize object attributes.
    def __init__(self, health, energy):
        # Attributes belong to the instance (self)
        self.health = health
        self.energy = energy


    # --------------------------------------------------------
    # __len__
    # --------------------------------------------------------
    # Called when len(object) is used
    def __len__(self):
        return self.health


    # --------------------------------------------------------
    # __abs__
    # --------------------------------------------------------
    # Called when abs(object) is used
    def __abs__(self):
        return self.energy


    # --------------------------------------------------------
    # __call__
    # --------------------------------------------------------
    # Allows the object to be called like a function
    def __call__(self):
        print("The monster was called!")


    # --------------------------------------------------------
    # __add__
    # --------------------------------------------------------
    # Called when object + other is used
    def __add__(self, other):
        return self.health + other


    # --------------------------------------------------------
    # __str__
    # --------------------------------------------------------
    # Called when print(object) or str(object) is used
    # Must return a string
    def __str__(self):
        return "Str dunder method was called"


    # --------------------------------------------------------
    # Normal instance methods
    # --------------------------------------------------------
    def attack(self, amount):
        print("Monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(f"Energy left: {self.energy}")


    def move(self, speed):
        print(f"Monster has moved at speed {speed}")


# ============================================================
# Creating an object
# ============================================================

monster1 = Monster(10, 20)

# ============================================================
# Using dunder methods
# ============================================================

# __str__ -> print(object)
print(monster1)

# __len__ -> len(object)
print(len(monster1))

# __abs__ -> abs(object)
print(abs(monster1))

# __call__ -> object()
monster1()

# __add__ -> object + value
print(monster1 + 55)

# ============================================================
# Introspection (examining the object)
# ============================================================

# vars() returns instance attributes as a dictionary
print(vars(monster1))

# __dict__ does the same thing
print(monster1.__dict__)

# dir() lists all attributes and methods (including dunders)
print(dir(monster1))
