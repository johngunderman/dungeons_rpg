
from actor import Actor
import random
import helper

class Enemy (Actor):

    def __init__(self, position, dimensions=(50,50), screen=None):
        super(Enemy, self).__init__(position, dimensions, screen)



class EvilMage (Enemy):

    def __init__(self, position, dimensions=(50,50), screen=None):
        super(EvilMage, self).__init__(position, dimensions, screen)
        self.load_image("amg1_fr1.gif", -1)
        self.screen.dirtied(self)
        
