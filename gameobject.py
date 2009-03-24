
import pygame
from pygame import Surface

class GameObject (object):
    """This class is the base class for anything that wants to find itself
    on the screen."""
    
    def __init__(self, position, dimensions=(100,100), screen=None):
        #print position, dimensions
        #TODO: eventually get sprites working
        self.dimensions = dimensions #(x,y)
        self.screen = screen
        self.position = position #(x,y)
        #FIXME: This is temporary until we get sprites up and running.
        self.surface = Surface(dimensions)
        self.color = pygame.Color("red")
        self.surface.fill(self.color)
        self.rect = pygame.Rect(self.position, self.dimensions)
        #self.rect = pygame.Rect(10,10,10,10)
        self.name = "Obj"
        #TODO: make "self.previous_location" an attribute

    def __str__(self):
        return "<GameObject: dimensions="+str(self.dimensions)+", position="+str(self.position)+">"

    def move(self, position):
        """Takes a position in (x,y) form and updates this object's position"""
        bak_rect = self.rect
        self.rect = pygame.Rect(position,self.dimensions)
        #print "move to " + str(self.rect)
        if not self.check_collisions():
            self.position = position
            self.screen.add_to_dirty_rects(bak_rect)
            self.screen.dirtied(self)
        else:
            self.rect = bak_rect
        #print self
           
        
    def check_collisions(self):
        """Check collisions between this object and all other objects in
        self.screen. This method is a wrapper for 
        self.screen.check_collisions()
        returns bool: True if collided, False if not."""
        if not self.screen.in_bounds(self):
            return True
            
        obj = self.screen.check_collisions(self)
        #print obj
        if obj is None: #no collision
            return False
        else:
            print "collision has occurred with " + str(obj)
            #TODO: handle collision
            return True
        
    def act(self):
        #TODO
        pass
        
    def collides_with(self, obj):
        """Checks whether or not this object collides with obj.
        True if collision, False if not."""
        #use pygame.Rect builtin collision routines
        return bool( self.rect.colliderect(obj) )
