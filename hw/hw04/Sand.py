from Particle import Particle
from Grid import Grid

class Sand(Particle):

    def is_move_ok(self, x,y):
        
        #check if coordinates are within grid bounds:
        if not (0 <= x < self.grid.width and 0 <= y < self.grid.height): 
            return False
            
        #check if space is not empty
        if self.grid.get(x,y) is not None:
            return False
        
        #check diagonal spaces, only if they are next to x
        if x != self.x and (x <= self.x + 1 or x >= self.x - 1):
            # not only check space its moving to but the space above it (might be blocking from corners)
            if self.grid.get(x,y-1) is not None:
                return False
            
        return True


    def physics(self):
        #return tuple of coordinates where the sand should move to. If invalid return None

        #try to move straight down, 
        if self.is_move_ok(self.x,self.y + 1):
            return (self.x, self.y + 1)
        #then diagonal left and down, 
        if self.is_move_ok(self.x - 1, self.y + 1):
            return (self.x - 1, self.y + 1)
        #then diagonal right and down
        if self.is_move_ok(self.x + 1, self.y + 1):
            return (self.x + 1, self.y + 1)
        
        return None