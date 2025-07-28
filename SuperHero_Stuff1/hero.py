# Lab 6 - Marvin M

import random

from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
      '''Initialize Hero with a name and health values'''
      self.name = name
      self.starting_health = starting_health
      self.current_health = starting_health
      self.armors = []
      self.abilities = []

    def battle(self, opponent):
        '''fight another hero and randomly choose a winner'''
        winner = random.choice([self.name, opponent.name])
        print(f"The winner is {winner}!")

    def add_ability(self,ability):
        '''Apends an ability to a hero's list of abilities.'''
        self.abilities.append(ability)

    def sum_attacks(self):
        total_damage = 0
        for abilities in self.abilities:
            total_damage += abilities.attack()
            return total_damage
        
    def add_armor(self, armor):
            '''Apend an armor to a hero's list of armors.'''
            self.armors.append(armor)
            print(f"{armor} has been added to the list of armors.")

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("batman", 300)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
    ability1 = Ability("explosion", 300)
    ability2 = Ability("Electrocution", 150)
    ability3 = Ability("Web shooter", 50)
    ability4 = Ability("Punch", 15)
    my_hero.add_ability(ability1)
    my_hero.add_ability(ability4)
    my_hero2.add_ability(ability2)
    my_hero2.add_ability(ability3)
    print(my_hero.abilities)
    print(my_hero2.abilities)