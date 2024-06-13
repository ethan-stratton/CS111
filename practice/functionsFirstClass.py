def double(x):
    return x+x
def triple(x):
    return x+x+x


myList = [double, triple, lambda x,y: x+y]

# myList.append(double)
# myList.append(triple)

def randFunc():
    import random
    return myList[random.randint(0, len(myList)-1)]

mystery = randFunc
print(mystery()) # randomyl picks function in myList, but not called because no num
print(mystery()(5)) #randomly calls double or triple on 5, based on the functions in the list

# for num in range(len(myList)):
#     print(myList[num](5))

