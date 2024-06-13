class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        """
        # create a list of length height and each element will be a list of length width
        #Each element of the inside lists should begin as None. 
        #Each Grid instance will keep track of these three values with instance attributes called width, height and array.
        #Hint: List concatenation could be helpful for creating our array.
        self.array = []
        for _ in range(width):
            row = []
            for _ in range(height):
                row.append(None)
            self.array.append(row)

        self.width = width
        self.height = height

    def __str__(self):
        """
        Grid(<height>, <width>, first = <first element>)
        """
        return f"Grid({self.height}, {self.width}, first = {self.get(0,0)})" # problem?

    def __repr__(self):
        """
        The __repr__ function is supposed to return a string that if 
        we pasted it into a Python script or called Python's eval() function, 
        would recreate the object. We don't yet have everything in this class we need to do that. 
        You'll add that part of the class in Homework 3. 
        For now, just have __repr__ return the same value as the __str__ method.
        """
        return f"Grid({self.height}, {self.width}, first = {self.get(0,0)})" 
    
    def __eq__(self, other):
        """
        The __eq__ dunder method is what python calls when you use the == operator to compare the instances of class. 
        Compares two Grids and decide if the arrays are the same size and contain the same values.
        First: it should check to see if other is another Grid object (use Python's isinstance() function). If not, it should return False.
        Second: return self.array == other.array. This will check both:
                1. That self and other have the same dimensions
                2. That each space in self and other match"""

        if isinstance(other, Grid):
            return self.array == other.array
        else:
            return False




    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if in_bounds(self, x, y):
            return self.array[x][y]
        else:
            raise IndexError("Set Value Error: X or Y is of inappropriate size")

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if in_bounds(self, x, y):
            self.array[x][y] = val
            return f"Point at {x}, {y} was set to {val}"
        else:
            raise IndexError("Set Value Error: X or Y is of inappropriate size")
            
        
def in_bounds(self, x,y):
        """
        Checks if the specified coordinates fit within the height and width of the array"""
        if x < 0 or x >= self.width:
            return False
        elif y < 0 or y >= self.height:
            return False
        else:
            return True


