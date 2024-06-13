from operator import mul
def double(x):
    return x * 2
def triple(x):
    return x * 3
def enigma (y):
    return double(triple(y)) + triple(triple(y))

def multiply_by(a):
    def slow_multiplication(b):
        sum = 0
        x=0
        while (x < a):
            sum = b + sum
            x=x+1 
        return sum
    return slow_multiplication

multiply_by_seven = multiply_by(7)
print(multiply_by_seven) #gets function name
print(multiply_by_seven(7))

