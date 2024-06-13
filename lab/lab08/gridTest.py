from Grid import Grid

if __name__ == "__main__":
    # something1 = Grid(5,10) # width, height
    # print(something1.width)
    # print(something1.height)
    
    # print(something1.get(4,9)) #x,y :: y must be <5

    # #print(something.set(1,9,"Debugging Value"))

    # print(something1)
    # #repr(something)

    # something2 = Grid(5,11)
    # something3 = Grid(5, 10)
    # print(something1 == something2)
    # print(something1 == something3)

    grid = Grid(6, 2)
    grid.set(0, 0, 1)
    print(grid.get(0,0))
    print(str(grid))



