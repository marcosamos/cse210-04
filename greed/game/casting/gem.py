# will be used to add up points from gem or rocks

from game.casting.actor import Actor

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40

""" Class Gem is passing the argument actor like a intance of Class actor """
class Gem(Actor):
    
    def __init__(self):
        super().__init__()
        pass