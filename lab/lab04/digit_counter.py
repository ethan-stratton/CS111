def digit_counter(func, num):
    """Return the number of digits when func(num) is true
    
    Write some print statements in this code to track what's happening in the function.
    Write some code that will test the function with different numbers with the is_even 
    function. Proceed to fix the digit_counter function.
    """
    counter = 0
    print("Starting digit_counter function with num =", num)
    
    while num > 0: # previously was infinite loop
        print("Current num value:", num)
        if func(num % 10):
            print("Function func(", num % 10, ") returned True")
            counter += 1
        else:
            print("Function func(", num % 10, ") returned False")
        num = num // 10
        print("Updated num value:", num)
    
    print("Exiting digit_counter function with counter =", counter)
    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""

# def main():
#     digit_counter(is_even,1112)

# if __name__ == "__main__":
#     main()