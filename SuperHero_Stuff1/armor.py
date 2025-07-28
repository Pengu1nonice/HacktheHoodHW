import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        '''returns a random value between 0 and max block'''
        return random.randint(0, self.max_block)
        
if __name__ == "__main__":
    shield = Armor("shield", 20)
    print(shield.block())