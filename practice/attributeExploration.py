from functools import cache

# if are tasked with doing something difficult
# aka doing attributes or decorators (which you've never seen before)
# go to the official python docs on it, or python wiki

# make a trace function

#write a function that takes in a function
# tracers print what the function does and prints if it's running

#this tracer can be a decorator
def tracer(func):
    
    def wrapper(*args): #takes any amount of numbers. If you want it to take any function then do *args. possible to limit to two or three etc.
        print(f"About to run '{func.__name__}' with {args}")
        result = func(*args)
        print(f"Successfully ran '{func.__name__}' and it returned {result}")
        return result #in this case, a + b
    return wrapper


# this is cacheing after you trace it, so it will only run the first time
#if you call it a ton of times

@cache # double wrapped with cache and tracer
@tracer # if you run "add" it also runs the tracer function automatically
def add(a,b): # check out line 33
    return a + b

#pass in "add", a function which takes two numbers
my_new_adder = tracer(add)

#adder runs the function you tell it to
final_result = my_new_adder(3, 4) 
print(f"Final result: {final_result}")

##does tracer automatically
add(5,9)

newAdd = cache(tracer(add))