def filter(lst, cond):
    """Returns a list where each element is an element where `cond(elem)` returns `True`.

    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> is_even = lambda x : x % 2 == 0 # Even numbers have remainder 0 when divided by 2.
    >>> filter(nums, is_even)
    [2, 4, 6, 8, 10]

    Implement a function filter that take in a list of integers lst and a function cond. 
    filter will return a list where the only elements in it are the elements in lst where 
    cond returned True for that element (i.e. cond(elem) is True). cond will be and should 
    be a one argument function that either returns True or False. 

    (You will not be implementing a cond function.)
    """
    # Return a list 
    # for each element if
    # the condition returns `True`.
    return [elem for elem in lst if cond(elem)]


def print_cond(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> print_cond(5)(is_even)
    2
    4
    """
    # function which takes one parameter cond
    def print_filtered(cond):
        # print out all integers from 1 to n 
        for i in range(1, n + 1):
            # where the condition is true
            if cond(i):
                print(i)

    # returns full function with cond and loop
    return print_filtered


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    #function with one parameter N
    def count_satisfying(N):
        #counts all the numbers from 1 to N 
        count = 0
        for i in range(1, N + 1):
            # does N satisfy the two conditions?

            #two-argument predicate function Condition:: 
            #the first argument is N and second argument is the
            # number from 1 to N (i)
            if condition(N, i):
                count += 1
        return count
    return count_satisfying


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    
    # def inner_print(x):
    #     if ________________________:
    #         print("done")
    #     else:
    #         print(x)
    #     return ____________________
    # return ________________________

    # and returns a repeatable print function that can print the next n parameters. 
    # After the nth parameter, it just prints “done”.
    
    # print_n takes in an integer n
    # inner_print takes in an additional thing x ()
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print


# OPTIONAL QUESTION
#####################

def make_repeater(func, n):
    """Return the function that computes the nth application of func.
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """



    def apply_n_times(x): # pass in number without func applied
        result = x
        for _ in range(n): #return nth application of func
            result = func(result) 
        return result
    return apply_n_times



##############################################

def test_filter():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_even = lambda x: x % 2 == 0
    assert filter(nums, is_even) == [2, 4, 6, 8, 10]

def test_print_cond():
    is_even = lambda x: x % 2 == 0
    # Redirect stdout for testing print statements
    import sys
    from io import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    print_cond(5)(is_even)
    printed_output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert printed_output == "2\n4\n"

def test_count_cond():
    count_factors = count_cond(lambda n, i: n % i == 0)
    assert count_factors(2) == 2

def test_print_n():
    # Redirect stdout for testing print statements
    import sys
    from io import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    f = print_n(2)
    f = f("hi")
    f = f("hello")
    f = f("bye")
    printed_output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert printed_output == "hi\nhello\ndone\n"

def test_make_repeater():
    add_three = make_repeater(lambda x: x + 1, 3)
    assert add_three(5) == 8

if __name__ == "__main__":
    #test_filter()
    #test_print_cond()
    #test_count_cond()
    #test_print_n()
    #test_make_repeater()
    #print("All tests passed!")

    f = print_n(2)
    f = f("hi")
    f = f("hello")
    f = f("bye")

    g = print_n(1)
    g = g("first")("second")("third")



