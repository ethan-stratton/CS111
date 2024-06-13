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
        # create a list of length height and each element will be a list of length width
        #Each element of the inside lists should begin as None. 
        self.width = width # x
        self.height = height # y

        # self.array = []
        # for _ in range(width):
        #     row = []
        #     for _ in range(height):
        #         row.append(None)
        #     self.array.append(row)
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
        #debugging
        return f"Grid.build({self.array})"
    
    def __eq__(self, other):
        """
        The __eq__ dunder method is what python calls when you use the == operator to compare the instances of class. 
        Compares two Grids and decide if the arrays are the same size and contain the same values.
        First: it should check to see if other is another Grid object (use Python's isinstance() function). If not, it should return False.
        Second: return self.array == other.array. This will check both:
                1. That self and other have the same dimensions
                2. That each space in self and other match"""
        #In the if statement that checks to see if other is an instance of Grid, 
        #add an elif clause to check if other is an instance of list. If it is, return self.array == other.

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
        #we already have build() and check_list_malformed() passing, so we just need to copy all the correct info in one line
        return deepcopy(self)

    @staticmethod
    def build(lst):
        """
        build() takes as input a nested list where each element in the outer list 
        is a row of the grid and each element in each of the nested list are the values for the columns.
        So a list that looks like this:
        >>> lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] """

        #Call check_list_malformed() on the passed in list. Do not do this in a try block. 
        #If that method throws an exception we want it to kill this method as well so we don't want to catch the exception here.
        Grid.check_list_malformed(lst)
        # Determine height and width of the grid from the len of the list object passed in (the height) and the length of one of the sub lists (the width).
        height = len(lst[0])
        width = len(lst)
        # Create a new Grid object with the height and width.
        new_grid = Grid(height, width)
        # Set the new Grid's array attribute to a deep copy of the list that was passed in. 
        new_grid.array = deepcopy(lst)
        # Return the newly created Grid object.
        return new_grid

    @staticmethod #allowed to call this without a Grid object
    def check_list_malformed(data):
        """
        This method will check to see that the passed in data 
        is in a valid format and throws an exception if it is not.
        """
        #The object passed in should be a list object
        if not isinstance(data, list):
            raise ValueError("Object is not of type 'list'")
        #The top-level list should not be empty
        if not data or data[0] is None:
            raise ValueError("Top row of list is empty.")
        
        #Each element of the list object should also be a list object
        for i in range(len(data)):
            if not isinstance(data[i],list): # is not passing here. 
                raise ValueError("One or more elements in the data is not a list object.")
            
        #Each element of the top-level list should have the same length
        #get length of first thing, compare it to lengths of all other lists
        top_level_length = len(data[0]) # [1, 2, 3] , top_level length is 3
        data_length = len(data)
        for i in range(data_length):
            if len(data[i]) < top_level_length:
                raise ValueError("The elements in the top level list do not have the same length.")
            
    def in_bounds(self, x, y):
            """
            Checks if the specified coordinates fit within the height and width of the array"""
            # if x < 0 or x >= self.width:
            #     return False
            # elif y < 0 or y >= self.height:
            #     return False
            # else:
            #     return True
            return 0 <= x <= self.width and 0 <= y <= self.height



def main():
    lst = [[(x, y) for x in range(4)] for y in range(3)]
    grid = Grid.build(lst)
    print(grid.width)
    print(grid.height)


    print(grid) #success
    debug1 = repr(grid)
    print(debug1) # success

    copy = grid.copy()
    print(copy) # success
    debug2 = repr(copy)
    print(debug2) # success

    # makes sure that a deep copy was made :: overwrites initial grid to be None in every position
    for y in range(3):
        for x in range(4): 
            grid.set(x, y, None)

    # print(grid)

    

    
    # width (x) should == 4, height(y) should == 3
    print(copy.width) # == 4, but equals 3
    print(copy.height) # == 3, but equals 4
    #they are switched for some reasons


    # for y in range(3):
    #     for x in range(4):
    #         assert copy.get(x, y) == (x, y)


if __name__ == "__main__":

    main()
    
