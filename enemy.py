
from actor import Actor
import random

class Enemy (Actor):

    def __init__(self, position, dimensions=(50,50), screen=None):
        super(Enemy, self).__init__(position, dimensions, screen)

    
        
