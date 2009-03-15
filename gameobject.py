
import pygame
from pygame import Surface

class GameObject (object):
    """This class is the base class for anything that wants to find itself
    on the screen."""
    
    def __init__(self, dimensions, position, screen=None):
        #TODO: eventually get sprites working
        self.dimensions = dimensions #(x,y)
        self.screen = screen
        self.position = position #(x,y)
        #FIXME: This is temporary until we get sprites up and running.
        self.surface = Surface(dimensions)
        self.color = pygame.Color("red")
        self.surface.fill(self.color)

    def __str__(self):
        return "<GameObject: dimensions="+str(self.dimensions)+", position="+str(self.position)+" >"

    def move(self, position):
        """Takes a position in (x,y) form and updates this object's position"""
        if not self.check_collisions():
            self.position = position
        
    def check_collisions(self):
        """Check collisions between this object and all other objects in
        self.screen. This method is a wrapper for 
        self.screen.check_collisions()
        returns bool: True if collided, False if not"""
        return self.screen.check_collisions(self)
        
    def collides_with(self, obj):
        """Checks whether or not this object collides with obj.
        True if collision, False if not."""
        return (not obj.position[0] >= self.position[0] #first check point collision from upper-left
            and not obj.position[1] >= self.position[1]
            and not obj.position[0] <= self.dimensions[0] + self.position[0] #now check from bottom-right
            and not obj.position[1] <= self.dimensions[1] + self.position[1]
            #make sure that the body does not collide either.
            and not obj.dimensions[0] + obj.position[0] <= self.dimensions[0] + self.position[0]
            and not obj.dimensions[1] + obj.position[1] <= self.dimensions[1] + self.position[1]
            )
            
