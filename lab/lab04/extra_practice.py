def largest_factor(n):
    """
    The following function finds the largest factor of a number n that is not n with the exception of n being 0 or 1.
    Factors are the numbers that divide by that n exactly without leaving any remainder. Factors of 8 are 1,2,4,8
    """

    if n <= 1:
        return n

    biggest_factor = 1
    #i = 2 
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            biggest_factor = i

    return biggest_factor

# print(largest_factor(0))# == 0
# print(largest_factor(2))# == 1
# print(largest_factor(1))# == 1
# print(largest_factor(3))# == 1
# print(largest_factor(4))# == 2
# print(largest_factor(8))# == 4 
# print(largest_factor(7))# == 1
# print(largest_factor(9))# == 3
# print(largest_factor(16))# == 8 
# print(largest_factor(25))# == 5

# largest_factor(8)# == 4 but returns 2, incorrect
# largest_factor(16)# == 8 but returns 4, incorrect



def missing_digits(n):
    """
    Given a number n that is in sorted, non-decreasing order, return the number of missing digits in n. 
    A missing digit is a number between the first and last digit of a that is not in n.

    For example, if missing_digits was to find the number of missing numbers in 34, 
    it would return 0 because there are no digits missing between 3 and 4. Other valid inputs include 1, 36, and 1489.
    752 would not be a valid input because it is in decreasing order.
    """
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = (last_digit - second_to_last_digit) -1 # -1 added to add space between numbers
        # don't add 0 or 1 to the counter. if diff is not 0 or 1, add it to the counter
        if diff <= 1:
            counter += 0 #do nothing
        else:
            counter += diff
        n //= 10

    print(counter)
    return counter


# missing_digits(33) #== 0
# missing_digits(1278) #== 4
# missing_digits(1122) #== 0
# missing_digits(9) #== 0



###extra code for first largest_factor() function. Wasn't able to get it to pass
# if n == 0:
#         print(0)
#         return 0
#     if n == 1:
#         print(1)
#         return 1
    
#     biggest_factor = n
#     i = 2

#     while i <= n ** 0.5:
#         if n % i == 0:
#             biggest_factor = i
#             n //= i  # Update n to its quotient for further factorization
#         else:
#             i += 1

#     # if n > 1:  # If n is a prime number
#     #     print(1)
#     #     return 1


#     # if biggest_factor == n:  # n is prime
#     #     print(1)
#     #     return 1

#     print(biggest_factor)
#     return biggest_factor
