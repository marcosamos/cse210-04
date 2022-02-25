# ### used to provide message over artifacts - 
# will be used to add up points from gem or rocks




from game.casting.actor import Actor


class Rock(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._pointminus = None
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._pointminus
    
    def set_message(self, pointminus):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._point = pointminus