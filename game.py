
from screen import Screen
from gameobject import GameObject
import pygame
from pygame.locals import *
from player import Player
from enemy import Enemy
from menu import Menu

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
        self.screen.add_object( self.player )
        #allow keys to be held down
        pygame.key.set_repeat(5,1) #milis delay, repeat
        while True:
            self.screen.update()
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



