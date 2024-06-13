from Grid import Grid

class Particle:

    def __init__(self, grid, x=0, y=0):
        self.x = x
        self.y = y
        self.grid = grid

    def __str__(self):
        # returns Particle(x,y) :: will return Sand(x,y) in the Sand class, Rock(x,y) in the Rock, etc.
        return f"{type(self).__name__}({self.x},{self.y})"
    
    def move(self):
        move_to = self.physics()

        #self.physics returns (<x>, <y>) or None
        if move_to is None:
            #exit the function if None
            return
        else:
            self.grid.set(self.x,self.y, None) #sets OG position to None

            new_x, new_y = move_to # unpack the tuple to get new x and y
            #Set the new position in the Grid to a reference to the Particle object (store self)
            self.x, self.y = new_x, new_y
            self.grid.set(self.x,self.y, self)
            

def main():
    grid = Grid(3,4)
    particle = Particle(grid, 1, 1)
        
    print(particle)

if __name__ == "__main__":
    main()