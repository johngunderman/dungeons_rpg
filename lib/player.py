
from actor import Actor
import random
import pygame
import helper
from pygame.locals import *

class Player (Actor):

    def __init__(self, position, dimensions=(50,50), screen=None):
        super(Player, self).__init__(position, dimensions, screen)
        self.name = "Player"
        self.load_image("avt1_fr2.gif", -1)

        
    def move(self, position):
        """Overrides actor so that we get random encounter generation."""
        #TODO: We need to limit random encounters to only certain areas on map.
        super(Player, self).move(position)
        event = random.randint(0,200)
        if event == 0:
            self.random_encounter()
    
    def act(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.move_up()
                if event.key == K_DOWN:
                    self.move_down()
                if event.key == K_LEFT:
                    self.move_left()
                if event.key == K_RIGHT:
                    self.move_right()
                if event.key == K_SPACE:
                    self.screen.main_menu()
                    
            
    def random_encounter(self):
        print "RANDOM ENCOUNTER!!!"
        
