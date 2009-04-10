
from gameobject import GameObject

class Actor (GameObject):

    def __init__(self, dimensions, position, screen=None):
        super(Actor, self).__init__(dimensions, position, screen)
        
        self.hp = 0
        self.xp = 0
        self.mana = 0
        self.level = 0
        self.attack = 0
        self.defense = 0
        self.sp_attack = 0
        self.sp_defense = 0
        
        self.known_moves = []
        
    def move_left(self):
        self.move((self.position[0] - 1,self.position[1]))
        
    def move_right(self):
        self.move((self.position[0] + 1,self.position[1]))
        
    def move_up(self):
        self.move((self.position[0],self.position[1] - 1))
        
    def move_down(self):
        self.move((self.position[0],self.position[1] + 1))
        

    
