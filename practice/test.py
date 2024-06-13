def multiply_by(a):
    def slow_multiplication(b):
        sum = 0
        x=0
        while (x < a):
            sum = b + sum
            x=x+1 
        return sum
    return slow_multiplication



a = multiply_by(2)

print(a)