def cascade(n):
    """
    123
    12
    1
    12
    123
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(123)



def inverse_cascade(n):
    """
    1
    12
    123
    12
    1
    """
    grow = lambda n: f_then_g(grow, print, n//10)
    shrink = lambda n: f_then_g(print, shrink, n//10)

    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)




    
