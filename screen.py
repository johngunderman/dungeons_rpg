
from pygame import display

class Screen (object):

    def __init__(self, dimensions):
        """Takes a coordinate pair (x,y) as dimensions, and constructs
        a screen on which all objects are displayed."""
        self.dimensions = dimensions
        display.init()
        self.surface = display.set_mode(dimensions)
        self.gameobjects = []
        
    def update(self):
        """Renders all elements and refreshes the display"""
        for obj in self.gameobjects:
            self.surface.blit(obj.surface, obj.position)
            
        #TODO: Eventually this should be replaced with
        #      The use of smart rect updating.
        display.flip()
        
    def add_object(self, gameobject):
        """Does exactly what it sounds like: adds a gameobject to this
        gamescreen"""
        self.gameobjects.append(gameobject)


