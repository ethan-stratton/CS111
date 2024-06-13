from random import randrange


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"
    if n >= 1 and n <= 100:
        #print(n)
        return True
    else:
        #print(n)
        return False




def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"

    # for i in range(1000):
    #     if not in_range1(randrange(1,102)):
    #         print("Got an Error.")
    #         i+=1
    #     else:
    #         i+=1
    
    for i in range(1000):
        n = randrange(1,102)
        try:
            in_range2(n)
            i+=1
        except ValueError as e:
            print(f"An Error occurred, type {type(e)}. Error: {e}")



def in_range2(num):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if num >= 1 and num <= 100:
        return None
    else:
        raise ValueError
    
if __name__ == "__main__":
    main()
