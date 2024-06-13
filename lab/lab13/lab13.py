def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    if n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

# print(skip_mul(1)) #== 1
# print(skip_mul(2)) #== 2
# print(skip_mul(5)) #== 15
# print(skip_mul(6)) #== 48
# print(skip_mul(8)) #== 384


def multiply(m, n):
    """ Takes two positive integers (including zero) and returns their product using recursion.

    Write a function that takes two numbers m and n and returns their product. 
    Assume m and n are positive integers including zero. Use recursion, not mul or *.

    Hint: 5*3 = 5 + (5⋅2) = 5 + 5 + (5⋅1).

    For the base case, what is the simplest possible input for multiply?

    For the recursive case, what does calling multiply(m - 1, n) do? 
    What does calling multiply(m, n - 1) do? What will the base case look like for each?

    >>> multiply(5, 3)
    15
    """

    if m == 0 or n == 0:
        return 0
    return m + multiply(m,n-1)

# print( multiply(0, 0))# == 0
# print( multiply(0, 3))# == 0)
# print( multiply(0, 4))# == 0)
# print( multiply(2, 0))# == 0)
# print( multiply(5, 0))# == 0)
# print( multiply(3, 1))# == 3)
# print( multiply(1, 7))# == 7)
# print( multiply(5, 3))# == 15)
# print( multiply(4, 7))# == 28)
# print( multiply(13, 12))# == 156)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    # What can we use to tell if a number is factor of another number: if it is divisible up to its square root
    # What is true when a number is prime?
    # What is true when a number is not prime?
    def is_prime_helper(n, divisor):
        if divisor * divisor > n:
            return True
        if n % divisor == 0:
            return False
        return is_prime_helper(n, divisor + 1)

    if n < 2:
        return False
    return is_prime_helper(n, 2) #starts with divisor at 2 and increments up

#assert is_prime(2)
#assert is_prime(3)
# assert not is_prime(4)
# assert is_prime(5)
# assert not is_prime(6)
# assert is_prime(7)
# assert is_prime(13)
# assert not is_prime(16)
# assert is_prime(31)
# assert not is_prime(35)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 0
    print(f"Starting hailstone function with: {n}")
    
    def hailstone_helper(n, count):

        if n % 2 == 0:
            n = n/2
            count +=1
            print(n)
        elif n == 1:
            #print(1)
            return 1
        else:
            n = (n * 3) + 1
            count +=1
            print(n)

        return hailstone_helper(n, count)
   
    hailstone_helper(n,count)

    # Pick a positive integer n as the start. If n is even, divide it by 2. 
    # If n is odd, multiply it by 3 and add 1. Continue this process until n is 1.
    # Write a function that takes a single argument with formal parameter name n, 
    # prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
    # Hint: When taking the recursive leap of faith, consider both the return value and side effect of this function.

#hailstone(7)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    #the statement below will return if m or n is one, thus closing off the loop
    if m == 1 or n ==1:
        return 1
    
    # explore both choices (move right or move up)
    return paths(m - 1, n) + paths(m, n - 1)

print(paths(2,2))
paths(5,7)
paths(117,1)
paths(1,157)

