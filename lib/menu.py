import pygame
from pygame.locals import *
from menu_item import MenuItem

class Menu (object):

    def __init__(self, position=(0,0), title="", menu_items={}, screen=None):
        self.position = position
        self.title = title
        #menu_items is a dictionary of menu entries paired to functions
        self.menu_items = menu_items
        self.screen = screen
        
        #the vertical pixels between menu items:
        self.separator = 5
        
        pygame.font.init()
        
        self.items = []
        
        #change None to a font if we want a specific font in the future
        self.font = pygame.font.Font( None, 22)
        #make our menu items
        for item in self.menu_items: 
             self.items.append( MenuItem(item, self.menu_items[item], self.font) )
        
        #make our title
        self.title_dimensions = self.font.size(self.title)
        self.title_surface = self.font.render(self.title, True, (255,255,255) )
        
        #the currently selected menu item
        self.selected = 0
        
        #figure out our total width and height:
        self.height = 0
        self.width = self.title_dimensions[0]
        for item in self.items:
            self.height += item.dimensions[1]
            if self.width < item.dimensions[0]:
                self.width = item.dimensions[0]
                
        #make sure to add in our separator:
        self.height += len(self.items) * self.separator
        
        
        
        
        
    def render(self):
        #our vertical pixel location
        x = 0
        #horizontal displacement
        y = 0
        
        s = pygame.Surface( (self.width, self.height) )
        s.fill( (0,0,255) )
        
        s.blit(self.title_surface, (x,y))
        y += self.title_surface.get_size()[1]
        
        print self.title_surface.get_size()
        print x, y
        
        print self.items
        
        for item in self.items:
            s.blit(item.render(), (x,y))
            y += item.dimensions[1] 
        return s
        
        
    def run(self):
        bak_surface = self.screen.surface.copy()
        
        while True:
            menu = self.render()
            rect = pygame.Rect(self.position, (self.width, self.height))
            self.screen.surface.blit(menu, self.position)
            pygame.display.update(rect)
            a = raw_input()
            if a == "":
                break
        
        self.screen.surface = bak_surface
