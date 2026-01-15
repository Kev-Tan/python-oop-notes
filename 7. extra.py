class Monster:
	# Docstring
	'''A monster that has some attributes'''
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy
		
        # Private attributes
		# Python cannot set private attributes, but private convention
		# dictates anything with underscore shouldn't be modified
		# Convention also applies to methods
		self._id = 5


	# methods 
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		self.energy -= 20
		
	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

monster = Monster(20, 10)

# hasattr and setattr
# hasattr checks whether an object has an attribute
print(hasattr(monster, 'weapon'))
if hasattr(monster,'health'):
	print(f'The monster has {monster.health} health')

# Set an attribute to a new value
# The same monster.weapon = 'Sword'
# Very useful for working with loops and creating attributes quickly
setattr(monster, 'weapon', 'Sword') 
print(monster.weapon)

new_attributes = (['Weapon', 'Axe'], ['Armor', 'Shield'], ['potion', 'mana'])
for attr, value in new_attributes:
	setattr(monster, attr, value)
# Print out the attributes
# print(vars(monster))

# doc
# Give documentation for our object, and explain code/classes to other people
# print(monster.__doc__)
help(str)