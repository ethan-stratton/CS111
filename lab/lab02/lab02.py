def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    #loop k: 
    #n = (n * n-1)
    m = 1
    for i in range(k):
        m *= (n-i)
    return m

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    a = map(int,str(y))

    return sum(a)


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] == '8' and n[i + 1] == '8':
            return True
    return False

# def main():
#     falling(5, 3)
#     sum_digits(1234)
#     double_eights(1294738844)

# if __name__ == "__main__":
#     main()