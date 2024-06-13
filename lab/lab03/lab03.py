def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    #takes a list s and returns a new list that keeps only the even-indexed elements of s 
    #and multiplies them by their corresponding index.
    #for number in list:
    #if i % 2, append i[i] to new list
    x = list()
    for i in range(len(s)):
        if i % 2 == 0:
            x.append(s[i] * i)
    return x
            

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    #try using list comprehension [<expression_to_add> for <element> in <sequence>] numbers = [i for i in range(5)]
    #[i**2 for i in [1, 2, 3, 4] if i % 2 == 0] ; [4, 16]
    #s[i], t[i]
    return [[s[i], t[i]] for i in range(len(s))]


def count_appearances(lst):
    """Returns a dictionary containing each integer's appearance count
    >>> lst = [0]
    >>> count_appearances(lst)
    {0: 1}
    >>> lst = [0, 0, 1, 2, 1, 1]
    >>> count_appearances(lst)
    {0: 2, 1: 3, 2: 1}
    >>> lst = [0, 0, 0, 0, 0, 3, 0, 0]
    >>> count_appearances(lst)
    {0: 7, 3: 1}
    """
    "*** YOUR CODE HERE ***"
    #make new dict, for each number in list:
    #if number is already in new dict, +=1
    # else add and set to one
    
    new_dict = {}
    for num in lst:
        if num in new_dict:
            new_dict[num] += 1
        else:
            new_dict[num] = 1
    return new_dict


def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    "*** YOUR CODE HERE ***"
    #opens the two files, reads the file specified by the input_filename line by line, 
    #and for each line it prints and writes to the file specified by the output_filename 
    #the line with the line number and colon prepended to it. This function does not return anything.

    #read input file, modify with loop and colon
    #write to output file
    with open(input_filename, 'r') as reading_file, open(output_filename, 'w') as output_file:
        #for each line in file_lines, write i: "stuff" to output file
        i = 1
        #Debug: print("Before loop")
        for line in reading_file:
            #Debug: print("Inside loop")
            new_formatted_line = f"{i}: {line}"
            output_file.write(new_formatted_line)
            print(new_formatted_line.strip())
            i += 1
        #Debug: print("After loop")

# def main():
#     copy_file('text.txt','output.txt')

# if __name__ == "__main__":
#     main()

########################################################
# OPTIONAL QUESTIONS

def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    # Write your code here
    #for each number from 1 to n, if that number modulu 0 is true, put into new list
    return sorted([x for x in range(1, n) if n % x == 0])

def slice_and_multiplice(lst):
    """Return a new list where all values past the first are
    multiplied by the first value.

    >>> slice_and_multiplice([1,1,6])
    [1, 6]
    >>> slice_and_multiplice([9,1,5,2])
    [9, 45, 18]
    >>> slice_and_multiplice([4])
    []
    >>> slice_and_multiplice([0,4,9,18,20])
    [0, 0, 0, 0]
    """
    # Write your code here
    #multiply every number after the first by the first
    first_element = lst[0]
    return [first_element * x for x in lst[1:]]
