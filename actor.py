
from gameobject import GameObject

class Actor (GameObject):

    def __init__(self, dimensions, position, screen=None):
        super(Actor, self).__init__(self, dimensions, position, screen)
        
    def move_left(self):
        self.move((self.position[0] - 1,self.position[1]))
        
    def move_right(self):
        self.move((self.position[0] + 1,self.position[1]))
        
    def move_up(self):
        self.move((self.position[0],self.position[1] - 1))
        
    def move_down(self):
        self.move((self.position[0],self.position[1] + 1))
        

    
