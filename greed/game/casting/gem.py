# ### used to provide message over artifacts - 
# now defines the Gem class which inherits from Actor
from game.casting.actor import Actor


""" Class Gem is passing the argument actor like a intance of Class actor """
class Gem(Actor):
    
    def __init__(self):
        super().__init__()
        pass