
from actor import Actor
import random
import pygame
import helper

class Player (Actor):

    def __init__(self, position, dimensions=(50,50), screen=None):
        super(Player, self).__init__(position, dimensions, screen)
        self.name = "Player"
        self.surface, self.rect = helper.load_image("avt1_fr2.gif", -1)
        
    def move(self, position):
        """Overrides actor so that we get random encounter generation."""
        #TODO: We need to limit random encounters to only certain areas on map.
        super(Player, self).move(position)
        event = random.randint(0,20)
        if event == 0:
            self.random_encounter()
            
    def random_encounter(self):
        print "RANDOM ENCOUNTER!!!"
        
