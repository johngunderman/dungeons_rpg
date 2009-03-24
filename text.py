import pygame
from gameobject import GameObject

class Text (GameObject):

    def __init__(self, position, text, screen=None):
        pygame.font.init()
        self.position = position
        self.text = text
        self.font = pygame.font.Font(None, 22)
        dimensions = self.font.size(text)
        super(Text, self).__init__(position, dimensions, screen)
        self.surface = self.font.render(self.text, True, (255,255,255) )
        
    def collides_with(self, gameobject):
        """No collisions for text."""
        return False
