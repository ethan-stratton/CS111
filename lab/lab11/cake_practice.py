def cake(): # Make sure you know when these print statements are executed!
    print('beets')
    def pie():
        print('sweets')
        return 'cake' # gets returned, not printed
    return pie

chocolate = cake()

chocolate

chocolate() # chocolate with the parentheses calls pie() inside cake()

more_chocolate, more_cake = chocolate(), cake # double assignment!
#more_chocolate has the parenthesses and calls pie()

more_chocolate


def snake(x, y): # Keep track of things on paper if you get lost.
    if cake == more_cake:
        return chocolate
    else:
        return x + y

snake(10, 20)

snake(10, 20)() #this calls pie() in cake()

cake = 'cake' # reassignment! goes to else statement in snake()
snake(10, 20)
