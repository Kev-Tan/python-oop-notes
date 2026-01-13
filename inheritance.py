# 1 class gets attributes/methods from one or multiple classes
# Child class gets attributes/methods from parent class
# This concept is called inheritance
# Improve reusability
# A class can inherit from an unlimited number of other classes


# class Monster:
#     def __init__(self, health, energy):
#         self.health = health
#         self.energy = energy

#     #methods
#     def attack(self, amount):
#         print("The monster has attacked!")
#         print(f'{amount} damage was dealt')
#         self.energy-=20

#     def move(self, speed):
#         print("The monster has moved")
#         print(f'It has a speed of {speed}')

# # To get inheritance, put bracket after class and put in the class you want to inherit from
# class Shark(Monster):
#     # Calling init from parents to get parents' attributes (old method)
#     def __init__(self, speed, health, energy):
#         Monster.__init__(self, health, energy)
#         self.speed = speed

#     def bite(self):
#         print('The shark has bitten')

#     # Function overriding
#     def move(self):
#         print("The shark has moved")
#         print(f"The speed of the shark is {self.speed}")

# shark = Shark(speed = 120, health = 100, energy = 80)
# print(shark.health)
# print(shark.speed, shark.health, shark.energy)

# New method for getting attributes from parents init
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    #methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy-=20

    def move(self, speed):
        print("The monster has moved")
        print(f'It has a speed of {speed}')

# # To get inheritance, put bracket after class and put in the class you want to inherit from
# # Much better approach
# class Shark(Monster):
#     # Calling init from parents to get parents' attributes (old method)
#     def __init__(self, speed, health, energy):
#         # Monster.__init__(self, health, energy)
#         super().__init__(health, energy)
#         self.speed = speed

#     def bite(self):
#         print('The shark has bitten')

#     # Function overriding
#     def move(self):
#         print("The shark has moved")
#         print(f"The speed of the shark is {self.speed}")

# shark = Shark(speed = 120, health = 100, energy = 80)
# print(shark.health)
# print(shark.speed, shark.health, shark.energy)

#Exercise
# Create scorpion class that inherits from monster
# Health and energy from the parent
# poison_damage attribute
# Overwite the damage method to show poison damage

class Scorpion(Monster):
    def __init__(self, scorpion_health, scorpion_energy, poison_damage):
        super().__init__(health = scorpion_health, energy = scorpion_energy)
        self.poison_damage = poison_damage

    def attack(self):
        print(f'Poison damage of value {self.poison_damage} is applied')


scorpion1 = Scorpion(scorpion_health=50, scorpion_energy=25, poison_damage=5)
scorpion1.attack()
scorpion1.move(10)
print(f'Scorpion health is {scorpion1.health}, energy is {scorpion1.energy}')