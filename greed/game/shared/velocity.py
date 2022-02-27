class Velocity:
    """
    Velocity set the object falling speeds
    """
    def __init__(self, dx, dy):
        """
        constructor speed represented as x and y
        """
        self._dx = dx  
        self._dy = dy  

    def get_x(self):
        """ gets and returns the horizontial distance
        shown in variable x
        """
        return self._dx

    def get_y(self):
        """gets and returns the vertical distance 
        shown in variable y
        """
        return self._dy

    def set_x(self, dx):
        """sets the hoizontail distance
        
        """
        self._x = dx

    def set_y(self, dy):
        """Sets the vertical distance.
        
        """
        self._y = dy
        
    def moveob(self, factor):
        """
        moves the object
        """
        return Velocity(self._dx * factor, self._dy * factor) 