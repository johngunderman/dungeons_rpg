from menu import Menu

class MainMenu (Menu):

    def __init__(self, screen):
        super(MainMenu, self).__init__(position=(20,20),
                                       title="Main Menu",
                                       menu_items={"Quit": self.quit,
                                             "Cancel": self.cancel
                                             },
                                       screen=screen
                                       )
                                       
    def quit(self):
        self.screen.kill()
        
    def cancel(self):
        return

