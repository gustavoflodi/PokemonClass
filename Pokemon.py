# Create object Pokemon, check status, increase health, make them battle and decide for a winner

class Pokemon:
   
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
    
    def __str__(self):
        return f"{self.name} ({self.primary_type}): {self.hp} / {self.max_hp}"
   
    def feed(self):
        if self.hp == self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += 1
    
    def battle(self, other):
        print("Battle", self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.hp = 0
            print(f"{self.name} fainted!")
        elif result == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f"{self.name} and {other.name} battled hard. It's a tie.")
        elif result == 'win':
            other.hp = 0
            print(f"{self.name} won. Congratulations!")
    
    @staticmethod
    def typewheel(type1, type2):
        result = {0: 'lose', 1: 'win', -1: 'tie'}

        game_map = {'water': 0, 'fire': 1, 'grass': 2}
        
        wl_matrix = [
            [-1, 1, 0], #water
            [0, -1, 1], #fire
            [1, 0, -1]  #grass
        ]
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        
        return result[wl_result]



if __name__ == '__main__':
    b = Pokemon(name='bulbasaur', primary_type='grass', max_hp=100)
    x = Pokemon(name='bulbasaur', primary_type='grass', max_hp=100)
    c = Pokemon(name='charmander', primary_type='fire', max_hp=150)
    b
    b.battle(c)
    print(b.hp)

"""
CONCEPTS
========
- Object-Oriented Programming in Python
- game logic
- instance methods
- `@staticmethod`
- self, other
- __init__, __str__
- if __name__ == '__main__'
- importing your own code
- breakpoint() debugging
"""
