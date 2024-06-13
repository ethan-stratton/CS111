from pair import Pair, nil

def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    def isPartofNum(c):
        return c in ("0123456789.")
    
    def findEndofNum(s, start):
        for i in range(start, len(s)):
            if not isPartofNum(s[i]):
                return i
        return len(s)

    answer = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i +=1
        elif isPartofNum(c):
            end = findEndofNum(expression, i)
            answer.append(expression[i:end])
            i = end
        else:
            answer.append(c)
            i += 1    
    return answer


def parse_tokens(tokens, index):
    """Takes a list of tokens and an index and converts the tokens to a Pair list.
    
    Args:
        tokens (list): List of tokens to parse.
        index (int): Current index in the token list.

    Returns:
        tuple: A Pair object representing the parsed tokens and the new index.

    Examples:
        >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
        (Pair('+', Pair(1, Pair(1, nil))), 5)
        >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
        (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    # 1. If the token at the provided index is an open parenthesis '('?
    if tokens[index] == "(":
        # 1.1 The next token should be an operator. Store the operator in a variable.
        #index +=1
        operator = tokens[index+1]

        # 1.2.0 If the index is not zero, then the current tokens is a start of a sub-expression, so...
        if index != 0:
            # 1.2.1 Call parse_tokens() by passing in the list of tokens with the index incremented by 2 (this puts the token after the operator as the next one to be processed). 
            # The recursive call will return two values: a new pair list and a new index respectively. Capture the new pair list returned by the function in a new variable and update index to the new index returned by the function.
            new_pair_list, index = parse_tokens(tokens, index+2)
            # 1.2.2 Set the variable you stored the operator in step 1.1 to a Pair object with the operator as .first and the new pair list (returned in step 1.2.1) as .rest
            operator = Pair(operator, new_pair_list)
       
        # 1.3 If the index of the current token is 0, increment the index by 2.
        if index == 0: 
            index +=2
        # 1.4 Call parse_tokens() with the token list and index. Update the index to new index returned by the function and capture the new pair list returned in a new variable. 
        # This function call will either return the rest of the syntax tree if the input index was 0 or nil if it wasn't.
        new_pair_list, index = parse_tokens(tokens, index)
        # 1.5 Return a Pair object with the variable from 1.1 (possibly updated in 1.2.2) as the .first and the pair list returned in step 1.4 as the .rest along with the index returned in 1.4 (in that order).
        return Pair(operator, new_pair_list), index


    # 2 If the token is a close parenthesis ')', return a nil object and the index incremented by 1.
    if tokens[index] == ")":
        return nil, index+1
        
        
    # 3 Everything else should be operands and should be integers or floating point numbers. 
    # Do this entire part in a try/except block that raises a TypeError if converting the current token to float or integer fails.
    try:
        # 3.1 If the current token has a decimal point, convert it to a float, and store it in a variable.
        if '.' in tokens[index]:
            current = float(tokens[index])
        # 3.2 If the current token does not have a decimal point, convert it to an int, and store it in a variable.
        else: # if '.' not in tokens[index]:
            current = int(tokens[index])
        # 3.3 Call parse_tokens() with the token list and the index incremented by 1 to process the next token. Capture the new pair list and update the index to the new index returned.
        new_pair_list, index = parse_tokens(tokens,index+1)
        # 3.4 Return a Pair object with the variable created in 3.1 or 3.2 as .first and the pair object returned in step 3.3 as .rest along with the index returned in step 3.3.
        return Pair(current, new_pair_list), index
    except ValueError:
        raise TypeError("Expected float or int")



# (* 6 (/ 2 4))
tokens = ['(', '*', '6', '(', '/', '2', '4', ')', ')']

key = (Pair('*', Pair(6, Pair(Pair('/', Pair(2, Pair(4, nil))), nil))), 9)

my_answer = parse_tokens(tokens, 0)

print(my_answer)
print(key)

# tree = parse_tokens(['(', '+', '1', '1', ')'], 0)
# print(tree)

# (+ 1 1) --> ['(', '+', '1', '1', ')'] --> Pair('+', Pair(1, Pair(1, nil)))

# (+ 1.5 1.5) --> ['(', '+', '1.5', '1.5', ')'] --> Pair('+', Pair(1.5, Pair(1.5, nil)))