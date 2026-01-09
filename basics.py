# We use camelCase for classes as a convention
class Monster:
    # attributes
    health = 90
    energy = 40

    # methods
    #1st parameter is reference to the class itself
    #It's often named self as a convention
    def attack(self, amount):
        print("Monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print(f'Monster has moved at speed {speed}')

#Turning it to object
monster = Monster() #The different naming scheme makes it clear what is an object and what is a class
monster.attack(40)
monster.move(30)