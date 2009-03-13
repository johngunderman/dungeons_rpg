
from screen import Screen

class Game (object):

    def __init__(self):
        """Game encompasses the entirety of all game states/objects/etc.
        Here we make our game screen and init some variables for holding our
        game objects."""
        self.screen = Screen((800,600))
        self.gameobjects = []
    
    def run(self):
        print "blah"


