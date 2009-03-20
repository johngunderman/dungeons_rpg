
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
        self.__backup_pos = self.position
        self.position = position
        if self.check_collisions():
            self.position = self.__backup_pos    
        
    def check_collisions(self):
        """Check collisions between this object and all other objects in
        self.screen. This method is a wrapper for 
        self.screen.check_collisions()
        returns bool: True if collided, False if not."""
        if not self.screen.in_bounds(self):
            return True
            
        obj = self.screen.check_collisions(self)
        print obj
        if obj is None: #no collision
            return False
        else:
            print "collision has occurred with " + str(obj)
            #handle collision
            return True
        
    def act(self):
        pass
        
    def collides_with(self, obj):
        """Checks whether or not this object collides with obj.
        True if collision, False if not."""
        #either we are to the left or right or above or below
        #important to note that in this method, self is the collidee, not the
        #collider. obj is the object we are moving around
        return not ((self.position[0] + self.dimensions[0] < obj.position[0])
                 or (self.position[0] > obj.position[0] + obj.dimensions[0])
                 or (self.position[1] + self.dimensions[1] <= obj.position[1])
                 or (self.position[1] > obj.position[1] + obj.dimensions[1])
                )
            
