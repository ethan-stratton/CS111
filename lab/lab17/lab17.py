import re


def cs_classes(post):
    """
    Returns a True or False if post contains strings in the form
    “CS111”, “CS 111”, and “C S 111” with optional spaces after the C and the S.  
    It should also match an optional “R” at the end of the number. 

    >>> cs_classes("Is it unreasonable to take CS111 in the summer?")
    True
    >>> cs_classes("how do I become a TA for C S 111? That job sounds so fun!")
    True
    >>> cs_classes("Can I take ECON101 as a CS major?")
    False
    >>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
    False
    >>> cs_classes("What are some good CS upper division courses? I was thinking about C S111R")
    True
    """
    return bool(re.search(r'C\s*S\s*111R?', post))
    #              C (any spaces) S (any spaces) 111 (R - optional) 

def roman_numerals(text):
    """
    Finds any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M).

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    ['IIV', 'VI', 'IV']
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    ['I', 'II', 'IV']
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    ['I', 'II', 'III', 'IV', 'V']
    >>> roman_numerals("Let's play Civ VII")
    ['VII']
    >>> roman_numerals("i love vi so much more than emacs.")
    []
    >>> roman_numerals("she loves ALL editors equally.")
    []
    """
    return re.findall(r"\b[IVXLCDM]+\b", text) # \b(?:[IVXLCDM]+)\b
    # \b saves whole words, not just one at a time. the + sign says we can have as many as we need


def match_time(text):
    """
    >>> match_time("At 05:24AM, I had sesame bagels with cream cheese before my coffee at 7:23.")
    ['05:24AM', '7:23']
    >>> match_time("At 23:59 I was sound asleep as the time turned to 00:00.")
    ['23:59', '00:00']
    >>> match_time("Mix water in a 1:2 ratio with chicken stock.")
    []
    >>> match_time("At 2:00 I pinged 127.0.0.1:80.")
    ['2:00']
    """
    return re.findall(r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:AM|PM)?\b", text) # \b(?:[01]?\d|2[0-3]):[0-5]\d(?:AM|PM)?\b
#(^[0-2]?)\d:\d\d(AM|PM)?
# ^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$
#^(?:[01]?\d|2[0-3])(?::[0-5]\d){1,2}$
# ^(?:\d|[01]\d|2[0-3]):[0-5]\d$
# ([0-2][0-3]|[0-1][0-9]):([0-5][0-9]{1}) only gets hour and minute
# ^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$

# Remove the ^ and $ anchors since they are used to match the start and end of a string, respectively.
# Add word boundaries (\b) to ensure we match whole words.



def area_codes(text):
    """
    Finds all phone numbers in text and captures the area code. Phone numbers
    have 10 digits total and may have parentheses around the area code, and
    hyphens or spaces after the third and sixth digits.

    >>> area_codes('(111) 111 1111, 1234567890 and 123 345 6789 should be matched.')
    ['111', '123', '123']
    >>> area_codes("1234567890 should, but 54321 and 654 456 78901 should not match")
    ['123']
    >>> area_codes("no matches for 12 3456 7890 or 09876-54321")
    []
    """
    return re.findall(r"\b\(?(\d{3})\)?[- ]?\d{3}[- ]?\d{4}\b", text)

    # needs to be surrounede by \b
    # optional opening parenthese \(?
    # capture three digits for the area code (\d{3})
    # optional closing parentheses \)?
    # An optional hyphen or space after the area code. [- ]? 
    # \d{3}: Exactly three digits for the central office code.
    # [- ]?: An optional hyphen or space after the central office code.
    # \d{4}: Exactly four digits for the line number.
    # \b: Word boundary to ensure the match is a whole word.


def most_common_code(text):
    """
    Takes in an input string which contains at least one phone number (and
    may contain more) and returns the most common area code among all phone
    numbers in the input. If there are multiple area codes with the same
    frequency, return the first one that appears in the input text.

    >>> most_common_code('(501) 333 3333')
    '501'
    >>> input_text = '''
    ... (123) 000 1234 and 12454, 098-123-0941, 123 451 0951 and 410-501-3021 has
    ... some phone numbers. '''
    >>> most_common_code(input_text)
    '123'
    """
    # call area_codes on the text
    # iterate over the returned list
    # if there are multiple same area codes, return that area code
    lst_of_area_codes = area_codes(text)
    frequency = {}

    for item in lst_of_area_codes:
        if item in frequency:
            frequency[item] +=1
        else:
            frequency[item] = 1

    max_count = -1
    max_area_code = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            max_area_code = item

    return max_area_code

input_text = '(123) 000 1234 and 12454, 098-123-0941, 123 451 0951 and 410-501-3021 are all phone numbers.'
print(most_common_code(input_text)) # == '123'

