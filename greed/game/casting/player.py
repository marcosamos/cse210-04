# inherit from the Actor class
from game.casting.actor import Actor

class Player(Actor):
    # player class will define/provide the points for the rock and gem

    def __init__(self):
        super().__init__()
        self._score = 0

    def rock_points(self):
        self._score -= 1

    def gem_points(self):
        self._score += 1
    
    def get_score(self):
        return(self._score)