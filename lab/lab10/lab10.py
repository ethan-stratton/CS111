from Grid import Grid
import random

def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces."""
    for y in range(grid.height):
        for x in range(grid.width):
            #prints x, y coordinates only if the coordinates exist. If they don't, print 0 (bc thats what the coordinates are)
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
            #This is an impure function, because it has side effects (multiple print statements)
        print()
    print()

def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    # #make a new copy of the grid in order to keep the programming functional
    # new_grid = Grid.copy(grid)
    # #Then loop over each slot in the grid copy. 
    # for y in range(new_grid.height):
    #     for x in range(new_grid.width):
    #         #If there is nothing in a slot, 
    #         if new_grid.get(x,y) == None:
    #             #randomly choose to add a rock, represented by the string 'r'. 
    #             if random() <= chance_of_rock:
    #                 new_grid.set(x,y, "r")

    # return new_grid
    new_grid = Grid.copy(grid)
    modify_grid(new_grid, lambda x,y : new_grid.set(x,y,"r"), chance_of_rock)
    return new_grid

def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    new_grid = Grid.copy(grid)
    #modify_grid(new_grid, lambda x, y: "b" if new_grid.get(x, y) is None else new_grid.get(x, y), chance_of_bubbles)
    modify_grid(new_grid, lambda x,y : new_grid.set(x,y,"b"), chance_of_bubbles)
    return new_grid

def modify_grid(grid, func, prob=None):
    """Update the grid using a function and a probability."""
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x,y) == None: 
                if prob is None or random.random() <= prob:
                    #current_value = grid.get(x, y)
                    # Pass x, y, and current_value to the lambda function
                    #new_value = func(x, y)
                    func(x,y)
                    #grid.set(x, y, new_value)

def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known to be able to bubble up and moves it up one row.
    The x and y coordinate should give you a bubble and moves the bubble one row up, 
    replacing its former position with None. Then it returns the modified grid. (Remember to use the copy() function)
    Note: You can assume the given x, y coordinate contains a bubble. Also, make sure you're not modifying the original grid.
    """
    new_grid = Grid.copy(grid)
    #replace coordinates with none      
    new_grid.set(x,y, None)
    if y-1 >= 0 and new_grid.get(x,y-1) != "b": # if there's no bubble above it and it didn't hit the ceiling
        #go up a row and replace it with bubble  
        new_grid.set(x, y-1, "b")
    else:
        #the bubble stays where it is
        new_grid.set(x,y,"b")
    return new_grid

def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    new_grid = Grid.copy(grid)
    #
    for y in range(new_grid.height):
        for x in range(new_grid.width):
            if new_grid.get(x, y) == "b":
                # Call bubble_up function to move the bubble up
                new_grid = bubble_up(new_grid, x, y)
    
    return new_grid


def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1


if __name__ == "__main__":
    """
    Create a small grid, call your random_rocks() function and assign the return value to a new name, 
    then call print_grid() to print the original and new grid. Are they the same? 
    You might want to pass in a fairly large value for chance_of_rock to make sure some rocks are created."""

    # grid = Grid(3, 4)
    # # print(grid)

    # # rocky_grid = random_rocks(grid, .3)
    # # print(rocky_grid)
    # # rocky_grid_visualized = repr(rocky_grid)

    # # print((rocky_grid_visualized))

    # debug_grid = repr(grid)
    # print(debug_grid)


    # bubbly_grid = random_bubbles(grid, .6)
    # # print(grid)
    # print(bubbly_grid)

    # debug_bubbly = repr(bubbly_grid)
    # print(debug_bubbly)

    #make grid, fill with bubbles, run move bubbles on it
    grid = Grid(4,5)
    bubbles = random_bubbles(grid, .4)

    debug = repr(bubbles)
    #print(debug)
    print_grid(bubbles)
    #animate_grid(bubbles, 2)


