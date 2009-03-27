import pygame
from pygame.locals import *

pygame.font.init() 


class MenuItem (object):

    def __init__(self, title, function, font):
        self.title = title
        self.function = function
        self.font = font
        self.dimensions = self.font.size(title)
        self.surface = self.font.render( title, True, (255,255,255) )
        
    def __repr__(self):
        return "<MenuItem(title="+str(self.title)+", function="+str(self.function)+")>"
        
    def execute():
        self.function()
        
    def render(self):
        return self.surface
        
