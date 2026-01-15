# ============================================================
# Functions are objects in Python
# ============================================================

# def test():
#     pass

# # Since a function is an object, you can store it in another variable
# a = test
# a.another_attribute = 10

# # You can see a function is an object with a __call__ dunder method
# print(dir(test))

# # You can see the added attribute shows up here too
# print(dir(a))


# ============================================================
# Passing functions into classes
# ============================================================

# def add(a, b):
#     return a + b


# class Test:
#     # Creating a function for an object by passing in another function
#     def __init__(self, add_function):
#         self.add_function = add_function


# test = Test(add_function=add)
# print(test.add_function(1, 2))


# ============================================================
# Functions as behavior (attack system example)
# ============================================================

# Create a Monster class with a parameter called attack_func
# Store this function as an attribute

# Create another class called Attacks that has 4 methods:
#   - bite
#   - strike
#   - slash
#   - kick
# (each method just prints text)

# Create a Monster object and give it one of the attack methods


class Monster:

    def __init__(self, attack_func, hp, energy):
        self.attack_func = attack_func
        self.hp = hp
        self.energy = energy


class Attacks:

    def bite(self):
        print("Bite opponent")

    def strike(self):
        print("Strike opponent")

    def slash(self):
        print("Slash opponent")

    def kick(self):
        print("Kick opponent")


# ------------------------------------------------------------
# Passing a method as an attack function
# ------------------------------------------------------------

attack_types = Attacks()

ghoul = Monster(
    attack_func=attack_types.slash,
    hp=50,
    energy=25
)

ghoul.attack_func()


# ------------------------------------------------------------
# Another way to do it (inline method passing)
# ------------------------------------------------------------

feral_wolf = Monster(
    attack_func=Attacks().bite,
    hp=20,
    energy=10
)

feral_wolf.attack_func()
