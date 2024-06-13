#from example import * 
# ^^^ import everything

from example import square, find_factors
import pytest

def test_square(): #black box testing
    assert square(4) == 16
    assert square(0) == 0
    #assert square(1/2) == 0.25, "The square of 1/2 is not 0.25"
    assert square(1/2) == pytest.approx(0.25)

# def test_square_root_raises_exception():
#     with pytest.raises(ValueError):
#         square_root(-4)

def test_find_factors():
    assert find_factors(15) == [1,3,5,15] #error
    assert find_factors(20) == [1,2,4,5,10,20]