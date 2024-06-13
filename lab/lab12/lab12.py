from operator import add, mul

# Write your code here for Q1 and Q2


def product(n):
    if not isinstance(n, int) or n < 1 :
        raise(ValueError)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result 


def summation(n):
    """
    summation that takes in a integer parameter n. 
    summation returns the result of 1 + 2 + ... + n; however, if n is less than zero or not an integer, raise a ValueError."""
    if not isinstance(n , int) or n < 1 :
        raise(ValueError)
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

def product_short(n):
    return accumulate(mul, 1, n)

def summation_short(n):
    return accumulate(add, 0, n)

def accumulate(merger, initial, n):
    """
    >>> from operator import add, mul
    >>> accumulate(add, 0, 3)  # 0 + 1 + 2 + 3
    6
    >>> accumulate(add, 2, 3)  # 2 + 1 + 2 + 3
    8
    >>> accumulate(mul, 2, 4)  # 2 * 1 * 2 * 3 * 4
    48
    >>> accumulate(mul, 5, 0)  # Raises a ValueError"""

    if not isinstance(n, int) or not isinstance(initial, int) or n < initial:
        raise ValueError("n must be equal to or greater than the initial value. Values must be integers")
        
    total = initial
    for i in range(1, n + 1):
        total = merger(total, i)
    return total

#############################################
# Q3

square = lambda x: x * x

sqrt = lambda x: x ** 0.5 # x^0.5 == √x

def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers) 
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        left_mid = len(numbers) // 2
        right_mid = left_mid + 1
        return mean([numbers[left_mid - 1], numbers[right_mid - 1]])
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers: # for each value in the dataset
        total_dist += square(num - avg) #find the data value minus the mean. Square result and add to sum

    return sqrt(total_dist / len(numbers)) #divide sum by size of dataset. take square root from previous step


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info = {}
    info["mean"] = mean(numbers)
    info["median"] = median(numbers)
    info["mode"] = mode(numbers)
    info["std_dev"] = std_dev(numbers)
    return info
    

#############################################
# (OPTIONAL) Write your code here for Invert and Change



def invert(x, limit):

    """Write the tests for a function invert that takes in a number x and limit as parameters. 
    invert calculates 1/x, and if the quotient is less than the limit, the function returns 1/x; 
    otherwise the function returns limit. However, if x is zero, the function raises a ZeroDivisionError.
    """

    if not isinstance(x, (int, float)) or not isinstance(limit, (int, float)):
        raise ValueError
    if x == 0:
        raise ZeroDivisionError
    
    inverted = float(1 / x)
    if inverted < limit:
        return inverted
    else:
        return limit
    
def change(x, y, limit):
    """
    Write the tests second function change that takes in numbers x, y and 
    limit as parameters and returns abs(y - x) / x if it is less than the limit; 
    otherwise the function returns the limit. If x is zero, raise a ZeroDivisionError.
    """
    # if not isinstance(x, (int, float)) or not isinstance(limit, (int, float)) or not isinstance(y,(int, float)):
    #     raise ValueError

    if not all(isinstance(arg, (int,float)) for arg in (x, y, limit)):
        raise ValueError

    if x == 0:
        raise ZeroDivisionError
    
    value = abs(y-x)
    result = value / x if value / x < limit else limit
    return result


def invert_short(x, limit):
    return limited(1, x, limit)

def change_short(x, y, limit):
    return limited(x, y, limit)

def limited(numerator, denominator, limit):
    """
    contain the logic of dividing a numerator by the denominator, and 
    if the result is greater than the limit then the function returns the 
    limit, and it returns the result otherwise. 
    However, if the denominator is zero, it raises a ZeroDivisionError.
    """
    if denominator == 0:
        raise ZeroDivisionError
    result = numerator / denominator
    # if result > limit:
    #     return limit
    # else:
    #     return result
    return limit if result > limit else result


    