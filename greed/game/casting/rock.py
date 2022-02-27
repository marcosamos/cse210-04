# ### used to provide message over artifacts - 
# now defines the Rock class which inherits from Actor

from game.casting.actor import Actor


class Rock(Actor):
    def __init__(self):
        super().__init__()
        pass
        # is pass needed here? 


#  ### old cold from RFK game - we don't need any of this correct? 
    # """
    # An item of cultural or historical interest. 
    
    # The responsibility of an Artifact is to provide a message about itself.

    # Attributes:
    #     _message (string): A short description about the artifact.
    # """
    # def __init__(self):
    #     super().__init__()
    #     self._pointminus = None
        
    # def get_message(self):
    #     """Gets the artifact's message.
        
    #     Returns:
    #         string: The message.
    #     """
    #     return self._pointminus
    
    # def set_message(self, pointminus):
    #     """Updates the message to the given one.
        
    #     Args:
    #         message (string): The given message.
    #     """
    #     self._point = pointminus