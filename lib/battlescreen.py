import pygame
from pygame.locals import *
from battlemenu import BattleMenu

class BattleScreen (object):

    def __init__(self, player, enemy, screen):
        #get a reference to the display (TONS easier than passing around a reference.)
        self.surface = pygame.display.get_surface()
        #give us our new background for battles.
        self.background = pygame.Surface(self.surface.get_size())
        self.background.fill((0,255,0))
        self.surface.blit(self.background, (0,0))
        self.screen = screen
        
        #TODO: draw our player and enemy.
        
        self.menu = BattleMenu(self.screen, self)
        self.menu.run()
        


