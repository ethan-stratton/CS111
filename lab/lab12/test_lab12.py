# Remember to import from the lab12 file and pytest
from lab12 import *
import pytest

# Write your test code here for Q1 and Q2

def test_product():
    assert product(5) == 120 # 1 * 2 * 3 * 4 * 5 = 120
    assert product(1) == 1
    with pytest.raises(ValueError):
        product(0) # make sure 0 raises ValueError
    with pytest.raises(ValueError):
        product(-5) # -5 is negative
    with pytest.raises(ValueError):
        product(3.5) #3.5 is a float, not int
    with pytest.raises(ValueError):
        product("some string") #string obv not accepted
    with pytest.raises(ValueError):
        product(None)
    

def test_summation():
    assert summation(10) == 55
    assert summation(1) == 1
    #test 0, test negatives, test different types, 
    with pytest.raises(ValueError):
        summation(0)
    with pytest.raises(ValueError):
        summation(-10)
    with pytest.raises(ValueError):
        summation(7.7)
    with pytest.raises(ValueError):
        summation("a string of characters")
    with pytest.raises(ValueError):
        summation(None)    

def test_accumulate():
    assert accumulate(add, 0, 3) == 6  # 0 + 1 + 2 + 3
    assert accumulate(add, 2, 3) == 8  # 2 + 1 + 2 + 3
    assert accumulate(mul, 2, 4) == 48 # 2 * 1 * 2 * 3 * 4

    with pytest.raises(ValueError):
        accumulate(mul, 5, 0) # Raises a ValueError"""
    with pytest.raises(ValueError):
        accumulate(mul, 4, "string") # Raises a ValueError"""
    with pytest.raises(ValueError):
        accumulate(mul, "string", 4) # Raises a ValueError"""


def test_product_short():
    assert product_short(4) == accumulate(mul, 1, 4)
    assert product_short(3) == accumulate(mul, 1, 3)

def test_summation_short():
    assert summation_short(3) == accumulate(add, 0, 3)
    assert summation_short(2) == accumulate(add, 0, 2)


# Q3
#####################################

def test_square():
    """Write your code here"""


def test_sqrt():
    """Write your code here"""


def test_mean():
    """Write your code here"""
    assert mean([1,2,3]) == 2
    assert mean([5,10,15,20]) == pytest.approx(12.5)
    with pytest.raises(AssertionError):
            mean([])
    

def test_median():
    assert median([1,2,3,4,5]) == 3
    assert median([0,9,2,7,4,8,2]) == 4
    assert median([1,2,3,4]) == pytest.approx(2.5)
    assert median([0,0,0, 0]) == 0 
    assert median([42]) == 42
    with pytest.raises(AssertionError):
        median([])
    with pytest.raises(AssertionError):
        median("not a list")


def test_mode():
    assert mode([1,1,1,2,3,4,5,6,7,8,9]) == 1
    assert mode([0,5,0,4,0,3]) == 0
    assert mode([5,5,5,4,4,4]) == 5
    assert mode([1.1,2.2,3.3,4.4,5.5,6.6,3.3]) == 3.3
    with pytest.raises(AssertionError):
        mode([])
    with pytest.raises(AssertionError):
        mode("not a list")


def test_std_dev():
    numbers = [1, 2, 3, 4, 5]
    assert std_dev(numbers) == pytest.approx(1.4142135623731) 

    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert std_dev(numbers) == pytest.approx(1.5556349186104)

    numbers = [5]
    assert std_dev(numbers) == 0 # Standard deviation should be 0 for a single value

    with pytest.raises(AssertionError):
        std_dev([])

    with pytest.raises(AssertionError):
        std_dev("not a list")



def test_stat_analysis():
    """Write your code here"""


# OPTIONAL
#####################################

def test_invert():
    """
    When writing the tests, make sure to consider all cases. For example, invert should do the following:

    If 1/x is less than the limit return 1/x
    If 1/x is greater than the limit return limit
    If x is zero, raise a ZeroDivisionError"""
    #test_invert_less_than_limit():
    assert invert(2, 1) == pytest.approx(0.5)

    #test_invert_greater_than_limit():
    assert invert(0.5, 0.75) == pytest.approx(0.75)

    #test_invert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        invert(0, 0.5)

#done testing invert()


def test_change():

    # more than limit
    assert change(1, 2, 0.5) == pytest.approx(0.5)

    # less than limit
    assert change(1, 2, 0.25) == pytest.approx(0.25)

    with pytest.raises(ZeroDivisionError):
        change(0, 2, 0.5)

#done testing change()

def test_invert_short():
    assert invert_short(2,1) == limited(1, 2, 1)
    assert invert_short(0.5, 0.75) == limited(1, 0.5, 0.75)


def test_change_short():
    assert change_short(1,2,3) == limited(1,2,3)
    assert change_short(1,2,0.5) == limited(1,2,0.5)

def test_limited():
    #numerator, denominator, limit
    #greater
    assert limited(1, 2, 0.4) == pytest.approx(0.4) 
    #less than
    assert limited(3, 4, 1) == pytest.approx(0.75)
    

    with pytest.raises(ZeroDivisionError):
        limited(1, 0, 3) # can't divide by zero

