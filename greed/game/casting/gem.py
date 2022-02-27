# ### used to provide message over artifacts - 
# will be used to add up points from gem or rocks




from game.casting.actor import Actor


class Gem(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._pointplus = None
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._pointplus
    
    def set_message(self, pointplus):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._point = pointplus