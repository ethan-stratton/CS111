def happy(text):
    return "☻" + text + "☻"

def sad(text):
    return "☹" + text + "☹"

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

def make_texter(emoji):
    def texter(text):
        return emoji + text + emoji
    return texter



msg1 = composer(sad, happy)("CS 111!")
msg2 = composer(happy, sad)("CS 240!")

msg3 = composer(happy, make_texter("☃︎"))('snow day!')


print(msg1)
print(msg2)
print(msg3)