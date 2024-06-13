from copy import deepcopy

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
        self.width = width
        self.height = height
        self.array = [[None for _ in range(width)] for _ in range(height)]

    def __str__(self):
        """
        Grid(<height>, <width>, first = <first element>)
        """
        return f"Grid({self.height}, {self.width}, first = {self.get(0,0)})" 

    def __repr__(self):
        """
        return a string that if we pasted it into a Python script or called Python's eval() function, 
        would recreate the object. 
        >>> repr(grid)
        'Grid.build([[1, 2], [3, 4]])'
        """
        return f"Grid.build({self.array})"
    
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
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            raise IndexError("Set Value Error: X or Y is of inappropriate size")

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y): 
            self.array[y][x] = val
            return f"Point at {x}, {y} was set to {val}"
        else:
            raise IndexError("Set Value Error: X or Y is of inappropriate size")
    
    def copy(self):
        """
        takes no parameters, returns a grid object which is a copy of the one this is invoked on
        """
        return deepcopy(self)

    @staticmethod
    def build(lst):
        """
        build() takes as input a nested list where each element in the outer list 
        is a row of the grid and each element in each of the nested list are the values for the columns.
        So a list that looks like this:
        >>> lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] """
        Grid.check_list_malformed(lst)
        height = len(lst[0])
        width = len(lst)
        new_grid = Grid(height, width)
        new_grid.array = deepcopy(lst)
        return new_grid

    @staticmethod 
    def check_list_malformed(data):
        """
        This method will check to see that the passed in data 
        is in a valid format and throws an exception if it is not.
        """
        if not isinstance(data, list):
            raise ValueError("Object is not of type 'list'")
        if not data or data[0] is None:
            raise ValueError("Top row of list is empty.")        
        for i in range(len(data)):
            if not isinstance(data[i],list):
                raise ValueError("One or more elements in the data is not a list object.")
        top_level_length = len(data[0]) 
        data_length = len(data)
        for i in range(data_length):
            if len(data[i]) < top_level_length:
                raise ValueError("The elements in the top level list do not have the same length.")
            
    def in_bounds(self, x, y):
            """
            Checks if the specified coordinates fit within the height and width of the array"""
            return 0 <= x <= self.width and 0 <= y <= self.height
        