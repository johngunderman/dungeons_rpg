from menu import Menu

class BattleMenu (Menu):

    def __init__(self, screen, battlescreen):
        super(BattleMenu, self).__init__(position=(300,20),
                                         title="Battle Menu",
                                         menu_options={"Attack": self.attack,
                                                       "Magic" : self.magic,
                                                       "Item" : self.item,
                                                       "Escape" : self.escape },
                                         screen=screen)
        self.battlescreen = battlescreen

    def attack(self):
        pass
        
    def magic(self):
        pass

    def item(self):
        pass
        
    def escape(self):
        pass
