def compose(f, g):
    #return lambda x:f(g(x))
    def composed(x):
        res = g(x)
        return f(res) #return x squared plus x squared (x=5)
    return composed
    
def add_to_self(x):
    return x + x

def square(x):
    return x * x

result = compose(add_to_self, square)(5) # add debug here
#
print(result)