"""
========================================
PYTHON NOTES: FUNCTIONS, CLASSES & OBJECT INTERACTION
========================================

This file demonstrates:
1. Why modifying global variables inside functions is bad practice
2. How objects store and update state
3. How methods interact between different objects (Hero attacking Monster)
4. How return values vs side effects work in class methods
"""

# -------------------------------------------------
# ❌ BAD EXAMPLE: modifying global variables
# -------------------------------------------------
# def update_health(amount):
#     health += amount
#
# health = 10
# update_health(20)
#
# ❌ This causes an error because:
# - 'health' inside the function is treated as a LOCAL variable
# - Python does not know you mean the global 'health'
#
# Workaround: use `global health` (NOT recommended)
# Better solution: store state inside objects (classes)


# -------------------------------------------------
# ✅ GOOD PRACTICE: MODIFY OBJECT STATE
# -------------------------------------------------

def update_health(amount):
    """
    This function modifies the monster object's health.
    The object is global, but the data is safely stored
    inside the object itself.
    """
    monster.health += amount


class Monster:
    """
    Monster class represents an enemy with health and energy.
    """

    def __init__(self, health, energy):
        # Instance variables
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        """
        Modifies the monster's energy.
        This method directly changes object state (side effect).
        """
        self.energy += amount

    def set_energy(self, energy):
        """
        Example showing RETURN vs SIDE EFFECT.

        This method RETURNS a value instead of directly
        modifying self.energy.
        """
        new_energy = energy * 2
        return new_energy


# Create monster object
monster = Monster(health=100, energy=50)

# Modify monster health using function
update_health(20)
print(monster.health)  # 120

# ❗ This returns a value but does NOT update self.energy
monster.set_energy(20)
print(monster.energy)  # Still 50


# -------------------------------------------------
# 📝 IMPORTANT LESSON:
# -------------------------------------------------
# If a method RETURNS something, you must ASSIGN it:
#
# monster.energy = monster.set_energy(20)
#
# Otherwise, nothing changes inside the object.


# -------------------------------------------------
# 🎯 EXERCISE IMPLEMENTATION
# Hero ↔ Monster Interaction
# -------------------------------------------------

class Hero:
    """
    Hero class represents a player character.
    """

    def __init__(self, damage, opponent):
        self.damage = damage          # How much damage hero deals
        self.opponent = opponent      # Reference to Monster object

    def attack(self):
        """
        Hero attacks the monster.
        Calls the monster's get_damage() method.
        """
        self.opponent.get_damage(damage=self.damage)


class Monster:
    """
    Monster class with health reduction logic.
    """

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def get_damage(self, damage):
        """
        Reduces monster's health when attacked.
        """
        self.health -= damage


# -------------------------------------------------
# 🧪 TEST THE INTERACTION
# -------------------------------------------------

monster1 = Monster(health=50, energy=25)
hero1 = Hero(damage=20, opponent=monster1)

print(monster1.health)  # 50
hero1.attack()
print(monster1.health)  # 30
hero1.attack()
print(monster1.health)  # 10


# -------------------------------------------------
# ✅ KEY TAKEAWAYS
# -------------------------------------------------
# 1. Objects store state (health, energy)
# 2. Methods modify state safely
# 3. One object can call another object's methods
# 4. Returning a value ≠ updating object state
# 5. Object-oriented design avoids global variables
