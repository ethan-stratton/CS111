t = (1, [2, 3])
t[1][0] = 4
t[1][1] = "Whoops"

print(t)

s = [2, 3]
t = [5, 6]
#s.extend(4) #int object not iterable
s.extend(t)
t = 0

print(s)
print(t)

##
print("new test")

L = [1, 2, 3, 4, 5]
print(L)

L[2] = 6
print(L)

L[1:3] = [9, 8]
print(L)

L[2:4] = []            # Deleting elements
print(L)

L[1:1] = [2, 3, 4, 5]  # Inserting elements
print(L)

L[len(L):] = [10, 11]  # Appending
print(L)

L = L + [20, 30]
print(L)

L[0:0] = range(-3, 0)  # Prepending
print(L)


print("new test")

#mutable value in parent frame can maintain local state for a function
def make_withdraw_account(initial):
    balance = [initial]
    
    def withdraw(amount):
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    
    return withdraw


"""
as a rule, Functions shouldn't be changing the values of variables passed in
This is considered a side effect
Instead of changing objects, they create copies with the new values and return those copies.  The original object remains unchanged.

"""
