from pair import nil, Pair
from operator import add, sub, mul, truediv as div

def tokenize(expr):
    return expr.replace("(", "( ").replace(")", " )").split()

def parse_with_index(tokens, index):
    """Takes a list of tokens and an index and converts the tokens to a Pair list.
        >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
        (Pair('+', Pair(1, Pair(1, nil))), 5)
        >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
        (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == "(":
        operator = tokens[index+1]
        if index != 0:
            new_pair_list, index = parse_with_index(tokens, index+2)
            operator = Pair(operator, new_pair_list)
        if index == 0: 
            index +=2
        new_pair_list, index = parse_with_index(tokens, index)
        return Pair(operator, new_pair_list), index

    if tokens[index] == ")":
        return nil, index+1
        
    try:
        if '.' in tokens[index]:
            current = float(tokens[index])
        else:
            current = int(tokens[index])
        new_pair_list, index = parse_with_index(tokens,index+1)
        return Pair(current, new_pair_list), index
    except ValueError:
        raise TypeError("Expected float or int")

def parse(tokens):
    # wrapper parses without returning index
    parsed_result, _ =  parse_with_index(tokens, 0)
    return parsed_result

    # def parse_rec(tok_iter):

    #     try:
    #         tok = next(tok_iter)
    #     except StopIteration:
    #         return None
        
    #     if tok == ")":
    #         return nil
    #     if tok == "(":
    #         return Pair(start_pairs(tok_iter), parse_rec(tok_iter))
        
    #     try: # only if we get a num
    #         num = float(tok) if '.' in tok else int(tok)
    #         return Pair(num, parse_rec(tok_iter))
    #     except ValueError:
    #         raise TypeError(f"I expected a num but instead got {tok}")
        
    # def start_pairs(tok_iter):
    #     try:
    #         operator = next(tok_iter)
    #     except StopIteration:
    #         return None
    #     return Pair(operator, parse_rec(tok_iter))
    
    # tok_iter = iter(tokens) # make iterator for the tokens
    # # next(tok_iter) # skips initial '(' at position 0
    # result = parse_rec(tok_iter)
    # print(result)

    # dads implementation: def parse(tokens):
    # def parse_rec(tok_iter):
    #     try:
    #         tok = next(tok_iter)
    #     except StopIteration:
    #         return nil

    #     if tok == "(":
    #         first = parse_rec(tok_iter)
    #         rest = parse_rec(tok_iter)
    #         return Pair(first, rest)
    #     elif tok == ")":
    #         return nil
    #     else:
    #         try:
    #             return Pair(float(tok) if '.' in tok else int(tok), parse_rec(tok_iter))
    #         except ValueError:
    #             return Pair(tok, parse_rec(tok_iter))

    # tok_iter = iter(tokens)
    # return parse_rec(tok_iter)

def reduce(func, pairs : Pair, value_so_far):
    '''
    The reduce() function should traverse the pair list, applying the function to all the 
    values in the pair list starting with the initial value. 

    For the first value in the operands list, call the function with the initial value and the list value and capture the 
    return value. For all later list elements, apply the function to the current list element 
    and the result from the previous step. Once all elements have been processed, return the final result.'''

    # base case, only one item in pair
    current = pairs
    while current != nil:
        value_so_far = func(value_so_far, current.first)
        current = current.rest
    return value_so_far

def apply(operator, pairs: Pair):
    if operator not in ['+','-','*','/']:
        raise TypeError("Bro, use the right operators. Operator invalid.")
    
    if operator == '+':
        return reduce(add, pairs, 0)
    if operator == '*':
        return reduce(mul, pairs, 1)
    if operator == '/':
        return reduce(div, pairs.rest, pairs.first)
    if operator == '-':
        return reduce(sub, pairs.rest, pairs.first)
    # // - integer division
    # % - the modulus operator
    # sqrt - the square root operator
    # pow - the exponent operator

def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float): # If the expression is a primitive type, return the value
        return syntax_tree

    # If the expression is a Pair object it is some sort of expression.
    if isinstance(syntax_tree, Pair):
        # If the first item in the Pair is a Pair itself, we have a subexpression.
        if isinstance(syntax_tree.first, Pair):
            # We need to call eval() on the first item in the Pair
            first = eval(syntax_tree.first)
            # We also need to evaluate all the items in the rest of tree that is defined by Pair. 
            rest = syntax_tree.rest.map(eval)
            # This will evaluate all the sub-expressions and replace them with their values. 
            # We can do this using the map() method that is part of the Pair class. 
            # Since the rest item in the Pair is a Pair object, we can just call .rest.map() and pass the eval function to it.
            return Pair(first, rest)
    
        # If the first item in the Pair is an operator
        if isinstance(syntax_tree.first, str): # if its a string there's a high chance of it being an operator
            # Apply eval() to the rest of the pair (using map() just like in 2.1.2) to get a Pair list with the operands as the values.
            results = syntax_tree.rest.map(eval)
            # Call our apply() function passing in the operator and the results of step 2.2.1. Return the results of apply().
            return apply(syntax_tree.first, results)
    
    if not isinstance(syntax_tree, Pair):
        raise TypeError("Sorry your syntax tree is wack.")

def run_program():
    print("Welcome to the CS 111 Calculator Interpreter.")
    running = True
    while running:
        prompt = input("calc >> ")
        # If the supplied string is the word exit, the program should stop.
        if prompt.lower() == "exit" or prompt.lower() == "e":
            print("Goodbye!")
            running = False
            break # exit()
        # Parse the supplied string and validate that it is a valid expression. If not, print an error and return to step 1.
        try:
            tokenized = tokenize(prompt)
            pair_object = parse(tokenized)
            # 6. Evaluate the valid expression to get the result
            evaluated = eval(pair_object)
            print(evaluated)
        except Exception as e:
            print(f"Error: {e}")
        # 8. Return to step 1...

if __name__ == "__main__":
    run_program()
