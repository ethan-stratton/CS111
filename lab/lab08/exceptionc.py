def a():
    print("entering a")
    b()
    print("leaving a")

def b():
    print("entering b")
    c()
    print("leaving b")

def c():
    print("entering c")
    raise ValueError("Error!!")