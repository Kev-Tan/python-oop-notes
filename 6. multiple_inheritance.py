"""
=====================================================
Python OOP Notes: Multiple Inheritance & MRO
=====================================================

Key ideas:
- A class can inherit from multiple parent classes
- Python resolves method calls using MRO (Method Resolution Order)
- super() follows the MRO, NOT just the immediate parent
- **kwargs allows flexible argument passing through the MRO chain

IMPORTANT:
- All commented explanations are intentional learning notes
- Code order matters for MRO
"""

# =====================================================
# Parent Class 1: Monster
# =====================================================

class Monster:
    """
    Monster base class.

    Uses **kwargs so it can participate in multiple inheritance
    without breaking other parent classes.
    """

    def __init__(self, health, energy, **kwargs):
        # kwargs stores extra named arguments
        # print(kwargs)

        self.health = health
        self.energy = energy

        # Pass remaining arguments to the next class in the MRO
        # ** converts dictionary to named arguments
        super().__init__(**kwargs)

    # -------------------------------
    # Methods
    # -------------------------------
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


# =====================================================
# Parent Class 2: Fish
# =====================================================

class Fish:
    """
    Fish base class.

    Demonstrates how multiple parent classes cooperate
    using **kwargs and super().
    """

    def __init__(self, speed, has_scales, **kwargs):
        # kwargs should be empty by this point if no more parents exist
        print(kwargs)

        self.speed = speed
        self.has_scales = has_scales

        # Continue passing control down the MRO chain
        super().__init__(**kwargs)

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")


# =====================================================
# Child Class: Multiple Inheritance
# =====================================================

class Shark(Monster, Fish):
    """
    Shark class inheriting from both Monster and Fish.

    MRO:
        Shark → Monster → Fish → object
    """

    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength

        # All parameters MUST be passed as keyword arguments
        # so they can flow correctly through **kwargs
        super().__init__(
            health=health,
            energy=energy,
            speed=speed,
            has_scales=has_scales
        )


# =====================================================
# Example Usage
# =====================================================

shark = Shark(
    bite_strength=50,
    health=200,
    energy=55,
    speed=120,
    has_scales=False
)

print(shark.speed)
shark.swim()
shark.attack(30)


# =====================================================
# MRO (Method Resolution Order)
# =====================================================

# What order are parent methods called?
# Python follows the C3 Linearization algorithm
# Order depends on the class declaration:
# class Shark(Monster, Fish)

# Uncomment to inspect:
# print(Shark.mro())

"""
Expected MRO:
[Shark, Monster, Fish, object]
"""
