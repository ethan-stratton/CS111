import sys

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def write_output(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(data)

def mergesort(lst1, lst2):
    """
    Input: two sorted lists
    Return value: single merged list that is still sorted

    Look at the first element of each list, pick the smallest, 
    remove it from the list (or move a pointer to the next index) and store that smallest value in the new list to be returned. 
    Continue to do this until one of the lists is empty. 

    At that point, you copy all the remaining elements from the other list into the merged list which is then returned.
    
    >>> mergesort([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> mergesort([1, 1, 1], [2, 2, 2])
    [1, 1, 1, 2, 2, 2]
    >>> mergesort([], [1, 2, 3])
    [1, 2, 3]
    >>> mergesort([4, 5, 6], [])
    [4, 5, 6]
    >>> mergesort([], [])
    []
    >>> mergesort([1, 3, 5], [1, 3, 5])
    [1, 1, 3, 3, 5, 5]
    """

    if not lst1: # if empty
        return lst2
    if not lst2: # if empty
        return lst1

    if lst1[0] < lst2[0]: 
        # check first values against each other, sort them by which is larger. 
        # remove first sorted item and recursively call sorting on all other elements

        return [lst1.pop(0)] + mergesort(lst1, lst2)
    else:
        return [lst2.pop(0)] + mergesort(lst1, lst2)
    
def test_mergesort():
    print(mergesort([1, 3, 5], [2, 4, 6])) # 1 2 3 4 5 6
    print(mergesort([1, 1, 1], [2, 2, 2])) # 1 1 1 2 2 2

def sorting(lst):
    """
    Input: any list
    Return Value: sorted list 

    Split the list in half, recursively call the function on both parts.
    Call mergesort function to merge the two sorted halves. 

    >>> sorting([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    >>> sorting([])
    []
    >>> sorting([1])
    [1]
    >>> sorting([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> sorting([2, 3, 1])
    [1, 2, 3]
    """

    # base case: the list only has one or less elements. We know that the list is sorted at this point (only has one value)
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    first_half = lst[:mid]
    second_half = lst[mid:]
    
    # split the lists over and over until they are one value or less
    sorted_first = sorting(first_half)
    sorted_second = sorting(second_half)

    # merge sort the tiny individual lists by comparing one value at a time
    return mergesort(sorted_first,sorted_second)

def test_sorting():
    print(sorting([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print(sorting([])) # []
    print(sorting([1])) # [1]
    print(sorting([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]
    print(sorting([2, 3, 1])) # [1, 2, 3]

def main(argv):
    """
    test_mergesort()
    test_sorting()
    #pass
    """

    input_file = argv[1]
    output_file = argv[2]

    data = read_input(input_file)
    
    if not isinstance(data, list):
        print("Input data must be a list.")
        return
    
    sorted_data = sorting(data)
    write_output(output_file, sorted_data)


if __name__ == "__main__":
    main(sys.argv)


