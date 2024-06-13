from pair import *


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

# fullNum = ...
#while i (numPos) == . or isinstance Num :
# i++
# return fullNum (100 or 100.0 or .5)

    # alternate method using .split() and .replace(), only able to be done in Python. Also a fragile solution and easily broken e.g. "  ) "
    # return expression.replace("(", "( ").replace(")", " )").split()



# OPTIONAL
def parse_tokens(tokens):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list.

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """

    def parse_rec(tok_iter):
        try:
            tok = next(tok_iter)
        except StopIteration:
            return nil

        if tok == "(":
            first = parse_rec(tok_iter)
            rest = parse_rec(tok_iter)
            return Pair(first, rest)
        elif tok == ")":
            return nil
        else:
            try:
                return Pair(float(tok) if '.' in tok else int(tok), parse_rec(tok_iter))
            except ValueError:
                return Pair(tok, parse_rec(tok_iter))

    tok_iter = iter(tokens)
    return parse_rec(tok_iter)


result = parse_tokens(['(', '+', '1', '1', ')'])
print(result)
