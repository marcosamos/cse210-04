class Velocity:
    """
    Velocity set the object falling speeds
    """
    def __init__(self, x, y):
        """
        constructor speed represented as x and y
        """
        self._x = x  
        self._y = y  

    def get_x(self):
        """ gets and returns the horizontial distance
        shown in variable x
        """
        return self._x

    def get_y(self):
        """gets and returns the vertical distance 
        shown in variable y
        """
        return self._y

    def set_x(self, x):
        """sets the hoizontail distance
        
        """
        self._x = x

    def set_y(self, y):
        """Sets the vertical distance.
        
        """
        self._y = y
        
    def moveob(self, factor):
        """
        moves the object
        """
        return Velocity(self._x * factor, self._y * factor) 