
import pygame
from pygame import display

class Screen (object):

    ##TODO: We need to layer the game-objects with an z coord, because otherwise
    ##      we will have our objects colliding with the background, etc.
    ##      Possible fix: gameobject.collides_with(obj) method

    def __init__(self, dimensions):
        """Takes a coordinate pair (x,y) as dimensions, and constructs
        a screen on which all objects are displayed."""
        self.dimensions = dimensions
        display.init()
        display.set_caption("Dungeon-RPG")
        self.surface = display.set_mode(dimensions)
        self.background = self.surface.copy()
        self.gameobjects = []
        
    def update(self):
        """Renders all elements and refreshes the display"""
        #clear the screen:
        self.surface.blit(self.background, (0,0))
        for obj in self.gameobjects:
            self.surface.blit(obj.surface, obj.position)
            
        #TODO: Eventually this should be replaced with
        #      The use of smart rect updating.
        display.flip()
        
    def add_object(self, gameobject):
        """Does exactly what it sounds like: adds a gameobject to this
        gamescreen"""
        self.gameobjects.append(gameobject)
        
    def kill(self):
        """Close the screen."""
        display.quit()

    def check_collisions(self, gameobject):
        """Checks collisions on this screen.
        returns gameobject collided with. None if no collision."""
        for obj in self.gameobjects:
            if obj.collides_with(gameobject):
                return obj
        return None
            
            
    def in_bounds(self, obj):
        """Checks if the given gameobject is in bounds."""
        print "Checking if "+ str(obj) +" is in bounds..."
        #first check in-bounds from upper-left
        return (obj.position[0] >= 0 
            and obj.position[1] >= 0 
            #now check from bottom-right
            #make sure that the body does not extend out of bounds either.
            and obj.dimensions[0] + obj.position[0] <= self.dimensions[0]
            and obj.dimensions[1] + obj.position[1] <= self.dimensions[1] 
            )

