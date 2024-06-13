
def merge(a, b):
    """
    iterative merge sort
    """
    i = 0
    j = 0
    answer = []

    while i < len(a) or j < len(b):
        # if the counter in list b has run over or 
        # as long as the counter in a hasn't run over and
        # item at I in A is bigger than item at J in B
        if len(b) == j or len(a) != i and a[i] < b[j]:
            answer.append(a[i])
            i += 1
        else:
            answer.append(b[j])
            j += 1

    return answer

# print(merge([7,8], [5, 6, 19, 35]))

def break_it_down(lst):
    # base case
    if len(lst) <= 1:
        return lst

    # do something
    

    # recurse
    mid = len(lst) // 2
    list1 = break_it_down(lst[:mid]) # breaks down lists til they are 1 value or less
    list2 = break_it_down(lst[mid:])

    return merge(list1, list2) 



print(break_it_down([10,7,4,1,12,8,5,3]))


