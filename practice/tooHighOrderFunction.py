def a():
    x = 7
    def b():
        y = 10
        def c():
            z=18
            return x * y * z
        return c
    return b

result = a()()()

print(result) #1260. function returns a function returns a function

