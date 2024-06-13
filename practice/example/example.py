def square(x):
    return x * x

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0: # if n divided by i's remainder is 0
            factors.append(i)

    return factors


#assert <condition>, "<some error message>"
# def test_square():
#     assert square(4) == 16
#     assert square(0) == 0
#     assert square(1/2) == 0.25, "The square of 1/2 is not 0.25"

# def test_find_factors():
#     assert find_factors(15) == [1,3,5,15] #error
#     assert find_factors(20) == [1,2,4,5,10,20]

#run pytest example.py or pytest example.py -v to learn more

# def main():
    
#     test_square()
#     test_find_factors()

# if __name__ == "__main__":
#     main()
