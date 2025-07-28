import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        '''returns a random value between 0 and max damage'''
        return random.randint(0, self.max_damage)
        