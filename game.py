
from screen import Screen
from gameobject import GameObject
import pygame
from pygame.locals import *
from player import Player

class Game (object):

    def __init__(self):
        """Game encompasses the entirety of all game states/objects/etc.
        Here we make our game screen and init some variables for holding our
        game objects."""
        self.screen = Screen((800,600))
        self.gameobjects = []
        self.player = Player( (50,50),(50,50) )
    
    def run(self):
        """The main game loop. Handles events"""
        self.screen.add_object( GameObject( (10,10),(50,50) ) )
        self.screen.add_object( self.player )
        self.screen.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.screen.kill()
                    #TODO: eventually have a prompt for saving, etc.
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print "UP"
                        self.player.move_up()
                    if event.key == K_DOWN:
                        print "DOWN"
                        self.player.move_down()
                    if event.key == K_LEFT:
                        print "LEFT"
                        self.player.move_left()
                    if event.key == K_RIGHT:
                        print "RIGHT"
                        self.player.move_right()
    
    def quit(self):
        """Quit the game."""
        exit()


