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
        
        #set the currently selected menu item:
        self.index_of_selected = 0
        self.selected = self.items[self.index_of_selected]
        
        #make our selector icon:
        self.selector = pygame.Surface((5,5))
        self.selector.fill((255,255,255))        
                
                
        #figure out our total width and height:
        self.height = 0
        self.width = self.title_dimensions[0]
        for item in self.items:
            self.height += item.dimensions[1]
            if self.width < item.dimensions[0]:
                self.width = item.dimensions[0]
                
        #make sure to add in our separator:
        self.height += len(self.items) * self.separator + 5
        #add space for selector icon + buffer on right side:
        self.width += 14
        
        
        
    def render(self):
        #our vertical pixel location (give us space for the selector icon)
        x = 10
        #horizontal displacement
        y = 0
        
        s = pygame.Surface( (self.width, self.height) )
        s.fill( (0,0,255) )
        
        s.blit(self.title_surface, (x,y))
        y += self.title_surface.get_size()[1]
        #print self.title_surface.get_size()
        #print x, y
        #print self.items
        
        for item in self.items:
            if item is self.selected:
                #add 3 to y so that the icon is centered with the text.
                s.blit(self.selector, (0,y+3))
            s.blit(item.render(), (x,y))
            y += item.dimensions[1] 
        return s
        
    def update(self):
        menu = self.render()
        rect = pygame.Rect(self.position, (self.width, self.height))
        self.screen.surface.blit(menu, self.position)
        pygame.display.update(rect)
    
    def move_selected_down(self):
        if self.index_of_selected < len(self.items) - 1:
            self.index_of_selected += 1
            self.selected = self.items[self.index_of_selected]
    
    def move_selected_up(self):
        if self.index_of_selected > 0:
            self.index_of_selected -= 1
            self.selected = self.items[self.index_of_selected]        
        
    def run(self):
        #save the state of our game surface
        bak_surface = self.screen.surface.copy()
        
        while True:
            self.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.screen.kill()
                if event.type == KEYUP:
                    if event.key == K_UP:
                        self.move_selected_up()
                    if event.key == K_DOWN:
                        self.move_selected_down()
                    if event.key == K_RETURN:
                        self.selected.execute()
                    if event.key == K_ESCAPE:
                        #restore the state of our game surface
                        self.screen.surface = bak_surface
                        self.screen.refresh_screen()
                        return
        
        
