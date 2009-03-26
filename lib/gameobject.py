
import pygame
from pygame import Surface
import os
from pygame.locals import *

class GameObject (object):
    """This class is the base class for anything that wants to find itself
    on the screen."""
    
    def __init__(self, position, dimensions=(100,100), screen=None):
        #TODO: eventually get sprites working
        self.dimensions = dimensions #(x,y)
        self.screen = screen
        self.position = position #(x,y)
        #FIXME: This is temporary until we get sprites up and running.
        self.surface = Surface(dimensions)
        self.color = pygame.Color("red")
        self.surface.fill(self.color)
        self.rect = pygame.Rect(self.position, self.dimensions)
        self.image = None
        self.name = "Obj"
        #TODO: make "self.previous_location" an attribute

    def __str__(self):
        return "<GameObject: dimensions="+str(self.dimensions)+", position="+str(self.position)+">"

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('sprites', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        self.surface = image
        self.dimensions = image.get_size()
        self.rect = pygame.Rect(self.position,self.dimensions)
        

    def move(self, position):
        """Takes a position in (x,y) form and updates this object's position"""
        bak_rect = self.rect
        self.rect = pygame.Rect(position,self.dimensions)
        #print "move to " + str(self.rect)
        if not self.check_collisions():
            self.position = position
            self.screen.dirtied(self)
            #where we've been
            self.screen.add_to_dirty_rects(bak_rect)
        else:
            self.rect = bak_rect
        #print self 
        
    def render(self):
        return self.surface
        
    def check_collisions(self):
        """Check collisions between this object and all other objects in
        self.screen. This method is a wrapper for 
        self.screen.check_collisions()
        returns bool: True if collided, False if not."""
        if not self.screen.in_bounds(self):
            return True
            
        obj = self.screen.check_collisions(self)
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
