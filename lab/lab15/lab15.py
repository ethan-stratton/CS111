# Note: The Tree implemenation is at the bottom of the file
# Please read the docstrings to learn how to interact with a Tree object.

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = Tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = Tree('roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = Tree(1, [Tree('berry',[Tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    # Write your code here
    # a tree object gets passed in
    if t.label == "berry": # base
        return True
    for branch in t.branches: # recursive case
        if berry_finder(branch):
            return True
    return False # end case

def sum_tree(t):
    """Sum all the labels in a tree"""
    total = t.label    
    for branch in t.branches:
        total += sum_tree(branch)

    return total

def sum_tree_alt(t):
    """Sum all the labels in a tree"""
    if t.is_leaf():
        return t.label
    else:
        total = 0
        total += t.label
        for branch in t.branches:
            branch_sum = sum_tree(branch)
            total += branch_sum

        return total


def height(t):
    """Return the height of a Tree. The height of a tree is the length of the longest path from the root to a leaf (starting at 0).

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    if t.is_leaf():
        return 0
    
    max_height = 0
    for branch in t.branches:
        max_height = max(max_height, height(branch))
    return max_height + 1

def max_path_sum(t):
    """Return the maximum path sum of the Tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    # go through each depth, return the highest one
    if t.is_leaf():
        return t.label

    max_sum = 0
    for branch in t.branches:
        max_sum = max(max_sum, max_path_sum(branch))
    
    return t.label + max_sum

def find_path(t, x):
    """
    Takes in a tree and a value x and returns a list containing the nodes along the path 
    required to get from the root of the tree to a node containing x.

    If x is not present in the tree, return None. 
    Assume that the entries of the tree are unique, so there will only be one path to node x.
    
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])] ), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    # Highlight the code and press Ctrl-'/' to unccomment the code all at once
    # if _____________________________:
    #     return _____________________________
    # _____________________________:
    #     path = ______________________
    #     if _____________________________:
    #         return _____________________________

    if t.label == x:
        return [t.label] # if node is correct label, return a list with the node in it
    for branch in t.branches:
        path = find_path(branch, x)
        if path is not None: # if it doesnt end, add this node to the path
            return [t.label] + path
    return None # if it doesnt exist return None
    


# Optional Question
def has_path(t, word):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular word.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'

    if t.label != word[0]: # if it doesn't match the first character, return false
        return False
    
    for branch in t.branches:
        if has_path(branch, word[1:]): # if any branch has the next remaining character, return True
            return True
        
    return False

    # alternative way to do this with an index
    
    # def _has_path_helper(tree, word, index):
    #     if index == len(word):
    #         return True  # Entire word is found along the path

    #     # Check if the current tree label matches the next character in the word
    #     if tree.label == word[index]:
    #         # Check all branches to find the next character in the word
    #         for branch in tree.branches:
    #             if _has_path_helper(branch, word, index + 1):
    #                 return True
    #     return False

    # # Start the recursion from the root of the tree
    # return any(_has_path_helper(branch, word, 0) for branch in t.branches)

class Tree:

    def __init__(self, label, branches=[]): # root, children
        """
        A Tree is constructed by passing a label and an optional *list* of branches.
        The list passed must only contain objects of the Tree class.
        """
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        """
        Returns a boolean, true if this Tree object is a leaf (has no branches), false otherwise.
        """
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{branch_str})'

    def __str__(self):
    
        def indented(self):
            lines = []
            for b in self.branches:
                for line in indented(b):
                    lines.append('  ' + line)
            return [str(self.label)] + lines

        return '\n'.join(indented(self))

