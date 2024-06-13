def print_ll_recursively(link):
    if link is Link.empty:
        return
    else:
        print(link.first)
        print_ll_recursively(link.rest)

def print_ll_iteratively(link):
    while link is not Link.empty:
        print(link.first)
        link = link.rest

def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements. This function is done iteratively

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    python_list = []
    while link is not Link.empty:
        python_list.append(link.first)
        link = link.rest
    return python_list

def convert_link_recursive(link):
    if link is Link.empty:
        return [] # return empty list
    else:
        return [link.first] + convert_link_recursive(link.rest)

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    def store_digits_helper(n):
        if n < 10:  # Base case: if n is a single digit
            return Link(n)
        else:
            last_digit = n % 10
            rest = store_digits_helper(n // 10)  # Recursively store the rest of the digits
            rest_last = rest
            while rest_last.rest is not Link.empty:
                rest_last = rest_last.rest
            rest_last.rest = Link(last_digit)
            return rest

    # Handle the special case where n is 0
    if n == 0:
        return Link(0)
    
    return store_digits_helper(n)


def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    current = link
    while current is not Link.empty and current.rest is not Link.empty:
        current.rest = current.rest.rest
        current = current.rest


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    current = link
    while current is not Link.empty:
        if isinstance(current.first, Link):
            deep_map_mut(fn, current.first)
        else:
            current.first = fn(current.first)
        current = current.rest


class Link:

    empty = () # empty tuple
    # Links only have two values, first and rest. Rest is just populated with other linked lists.
    # this is enforced by the assert statement. Linked Lists may only be populated with other linked lists.
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    


# Example convert_link
# link = Link(1, Link(2, Link(3, Link(4))))
# print(convert_link(link))  # Output: [1, 2, 3, 4]
# print(convert_link(Link.empty))  # Output: []



# Example store_digits
# store_digits(1) == Link(1)
# store_digits(2345) == Link(2, Link(3, Link(4, Link(5))))
# store_digits(876) == Link(8, Link(7, Link(6)))
# store_digits(0) == Link(0)

print(store_digits(2345))



# # Example every_other
# s = Link(1, Link(2, Link(3, Link(4))))
# every_other(s)
# print(s)  # Output: Link(1, Link(3))

# odd_length = Link(5, Link(3, Link(1)))
# every_other(odd_length)
# print(odd_length)  # Output: Link(5, Link(1))

# singleton = Link(4)
# every_other(singleton)
# print(singleton)  # Output: Link(4)



# # example deep_map_mut
# link1 = Link(3, Link(Link(4), Link(5, Link(6))))
# deep_map_mut(lambda x: x * x, link1)
# print(link1)  # Output: Link(9, Link(Link(16), Link(25, Link(36))))
