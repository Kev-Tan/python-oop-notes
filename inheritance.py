"""
=====================================================
Python OOP Notes: Inheritance
=====================================================

Key ideas:
- A child class can inherit attributes and methods from one or more parent classes
- This concept is called *inheritance*
- Inheritance improves code reusability
- A class can inherit from an unlimited number of other classes (multiple inheritance)

IMPORTANT:
- Commented code is intentionally kept as reference from previous exercises
- Comments ≠ useless code — they document learning progression
"""

# =====================================================
# Base Class (Parent)
# =====================================================

class Monster:
    """
    Base Monster class.

    Attributes:
        health (int): Monster's health points
        energy (int): Monster's energy points
    """

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # -------------------------------
    # Methods
    # -------------------------------
    def attack(self, amount):
        """
        Perform an attack that deals damage and consumes energy.
        """
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        """
        Move the monster with a given speed.
        """
        print("The monster has moved")
        print(f"It has a speed of {speed}")


# =====================================================
# OLD METHOD OF INHERITANCE (kept for reference)
# =====================================================

# class Shark(Monster):
#     """
#     Shark class inheriting from Monster (OLD init style).
#     """
#     def __init__(self, speed, health, energy):
#         Monster.__init__(self, health, energy)  # explicit parent call
#         self.speed = speed
#
#     def bite(self):
#         print("The shark has bitten")
#
#     # Method overriding
#     def move(self):
#         print("The shark has moved")
#         print(f"The speed of the shark is {self.speed}")
#
# shark = Shark(speed=120, health=100, energy=80)
# print(shark.health)
# print(shark.speed, shark.health, shark.energy)


# =====================================================
# MODERN / RECOMMENDED METHOD (super())
# =====================================================

# class Shark(Monster):
#     """
#     Shark class inheriting from Monster using super().
#     """
#     def __init__(self, speed, health, energy):
#         super().__init__(health, energy)  # preferred approach
#         self.speed = speed
#
#     def bite(self):
#         print("The shark has bitten")
#
#     # Method overriding
#     def move(self):
#         print("The shark has moved")
#         print(f"The speed of the shark is {self.speed}")
#
# shark = Shark(speed=120, health=100, energy=80)
# print(shark.speed, shark.health, shark.energy)


# =====================================================
# EXERCISE: Scorpion Class
# =====================================================

class Scorpion(Monster):
    """
    Scorpion class inheriting from Monster.

    Additional Attributes:
        poison_damage (int): Extra poison damage applied on attack
    """

    def __init__(self, scorpion_health, scorpion_energy, poison_damage):
        super().__init__(health=scorpion_health, energy=scorpion_energy)
        self.poison_damage = poison_damage

    # Method overriding
    def attack(self):
        """
        Override attack to apply poison damage.
        """
        print(f"Poison damage of value {self.poison_damage} is applied")


# =====================================================
# Example Usage
# =====================================================

scorpion1 = Scorpion(
    scorpion_health=50,
    scorpion_energy=25,
    poison_damage=5
)

scorpion1.attack()
scorpion1.move(10)

print(
    f"Scorpion health is {scorpion1.health}, "
    f"energy is {scorpion1.energy}"
)
