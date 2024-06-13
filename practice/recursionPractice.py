def recurse(x):
    print(f"recurse: {x}")
    if x == 10:
        return 0 # statement ends here, will always return 0 if x less than 10
    else:
        recurse(x + 1) # (return) recurse: None when recurse finishes, recurse doesn't return anything when it dissolves

#print(recurse(1)) # this returns None at the end

def recurse_mod(x):
    print(f"recurse_mod: {x}")
    if x == 10:
        return 0 
    else:
        return recurse_mod(x + 1) 
    
#print(recurse_mod(1)) # this returns 0 at the end, because we are using a return statement in the else: block

def add_digits(n): # slow, best used for small numbers as it decrements by 1
    if n == 0:
        return 0
    else:
        return n + add_digits(n-1) # return n + (n - 1) + (n - 1)...

#print(add_digits(5)) # 15

def r(n): # same function as above but one liner
    return n if n == 0 else n + r(n - 1)
    # returns n once n is 0, if n isn't 0, store the value of (n plus n - 1) til it hits zero.
#print(r(998)) # breaks recursion depth on my computer. possible to change with sys.setrecursionlimit()

def multiply(x, y):
    """
    takes two parameters, uses recursion to multiply"""
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y-1) # returns x plus x, y times

print(multiply(3,7))

def sum_of_digits(n: int) -> int:
    """
    If n is a single digit (0-9), the sum of its digits is n itself.
    Otherwise, the sum of the digits of n is the last digit of n plus the sum of the digits of n without the last digit.

    Steps to Solve the Problem:
        Base Case: If n is less than 10, return n.

        Recursive Case:
    Separate the last digit of n using n % 10.
    Reduce n by removing the last digit using integer division n // 10.
    Return the last digit plus the recursive call to sum_of_digits with the reduced number.
    """
    if n < 10:
        return n
    else:
        last_digit = n % 10
        all_digits_except_last = n // 10
        return last_digit + sum_of_digits(all_digits_except_last)
    
#print(sum_of_digits(12345)) # should be 15


def generate_subsequences(s: str) -> list:
    """
    generates all possible subsequences of a given string s.
    For example, the subsequences of "abc" are "", "a", "b", "c", "ab", "ac", "bc", "abc".
    """
    if not s:
        return [""]
    else:
        # Generate all subsequences of the string excluding the first character.
        first_char = s[0]
        rest_of_string = s[1:]

        rest_of_subsequences = generate_subsequences(rest_of_string)
        # For each subsequence generated, include both the subsequence itself and the subsequence with the first character appended to it.

        result = []
        for subsequence in rest_of_subsequences:
            result.append(subsequence)
            result.append(first_char + subsequence)

        return result


print(generate_subsequences("abc"))  
# Output: ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

print(generate_subsequences("ab"))   
# Output: ['', 'a', 'b', 'ab']