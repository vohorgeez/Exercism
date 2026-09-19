import random
import math

class Character:
    def __init__(self):
        self.strength = Character.ability(self)
        self.dexterity = Character.ability(self)
        self.constitution = Character.ability(self)
        self.intelligence = Character.ability(self)
        self.wisdom = Character.ability(self)
        self.charisma = Character.ability(self)
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        results = []
        for _ in range(4):
            results.append(random.randint(1,6))
        results.remove(min(results))
        return sum(results)

def modifier(value):
    return math.floor((value - 10)/2)