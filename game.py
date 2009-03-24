
from screen import Screen
from gameobject import GameObject
import pygame
from pygame.locals import *
from player import Player
from enemy import Enemy
from menu import Menu
from text import Text

class Game (object):

    def __init__(self):
        """Game encompasses the entirety of all game states/objects/etc.
        Here we make our game screen and init some variables for holding our
        game objects."""
        self.screen = Screen()
        self.gameobjects = []
        #NOTE: We have to specifically set screen to self.screen otherwise
        #      it will set dimensions to self.screen, which is BAD
        self.player = Player( (25,50), screen=self.screen )
    
    def run(self):
        """The main game loop. Handles events"""
        self.screen.add_object( Enemy( (0,0), screen=self.screen ) )
        self.screen.add_object( Text( (500,0), "Test", screen=self.screen) )
        self.screen.add_player( self.player )
        self.screen.run()
        #TODO: eventually have a prompt for saving, etc.
        self.quit()

    
    def quit(self):
        """Quit the game."""
        exit()



