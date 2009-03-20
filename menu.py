import pygame
from pygame.locals import *


class Menu (object):

    def __init__(self, position, title,  menu_items, screen=None):
        self.position = position
        self.title = title
        #menu_items is a dictionary of menu entries paired to functions
        self.menu_items = menu_items
        self.screen = screen
        
        pygame.font.init()
        
        self.items = []
        
        #change None to a font if we want a specific font in the future
        self.font = pygame.font.Font( None, 22)
        for title, function in self.menu_items:
             self.items.append( MenuItem(title, function, self.font) )
        
        
        
