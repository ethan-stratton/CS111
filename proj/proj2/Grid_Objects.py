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
    
class Rock(Particle):
    def physics(self):
        return None # well, it doesn't move, does it?
    
class Bubble(Particle): 

    def is_move_ok(self, x, y):
        if not (0 <= x < self.grid.width and 0 <= y < self.grid.height): 
            return False
        if self.grid.get(x,y) is not None:
            return False
        if x != self.x and (x <= self.x +1 or x >= self.x -1):
            if self.grid.get(x,y+1) is not None: #check corners
                return False
        return True

    def physics(self):


        import random
        randnum = random.randrange(0,300) # if we change this number to 300, it will only move a third of the time
        # extra implementation will be required though so the bubbles don't always go left


        if randnum < 30:# 30% chance
            #code to move the bubble to the right
            if self.is_move_ok(self.x + 1, self.y) :
                return (self.x + 1, self.y )

        if randnum < 45: #45 - 30  = 15% chance
            #code to move the bubble diagonally up and right
            if self.is_move_ok(self.x + 1, self.y - 1):
                return (self.x + 1, self.y - 1)

        if randnum < 55: 
            #code to move the bubble straight up
            if self.is_move_ok(self.x, self.y - 1):
                return (self.x, self.y - 1)

        if randnum < 70: 
            #code to move the bubble diagonally left and up
            if self.is_move_ok(self.x - 1, self.y - 1):
                return (self.x - 1, self.y - 1)

        if randnum < 100: # 30 percent chance
            #code to move the bubble left
            if self.is_move_ok(self.x - 1, self.y ):
                return (self.x - 1, self.y)
            
            #since the chances of moving are 1 in three hundred, we gotta check the other things again so they don't always move left
            
            if self.is_move_ok(self.x - 1, self.y - 1):
                return (self.x - 1, self.y - 1)
            if self.is_move_ok(self.x, self.y - 1):
                return (self.x, self.y - 1)
            if self.is_move_ok(self.x + 1, self.y - 1):
                return (self.x + 1, self.y - 1)
            if self.is_move_ok(self.x + 1, self.y) :
                return (self.x + 1, self.y )
            


    
    
        
        
        
        