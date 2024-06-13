class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __str__(self):
        """
        >>> str(b1)
        'A Tale of Two Cities by Charles Dickens'
        >>> print(b1)
        'A Tale of Two Cities by Charles Dickens' 
        :: recall that print() calls str()
        """
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """
        >>> repr(b1)
        "Book(0, 'A Tale of Two Cities', 'Charles Dickens')"
        """
        return f"Book({self.id}, '{self.title}', '{self.author}')"



class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library(b1, b2, b3)
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> b1.times_read
    1
    >>> b2.times_read
    2
    """

    def __init__(self, *args):
        """Takes in an arbitrary number of book objects and 
        puts them in a books dictionary which takes the book 
        id as the key and the book object as the value"""
        self.books = {}
        for book in args:
            self.books[book.id] = book


    def __str__(self):
        """
        str(l) == 'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'
        """
        # output_str = ""
        # for book in self.books.values():  # Iterate over values instead of keys
        #     output_str += str(book) + " | "
        # return output_str[:-3]  # Removes the trailing " | "
        return " | ".join(str(book) for book in self.books.values())

    def __repr__(self):
        """
        repr(l) == "Library(Book(0, 'A Tale of Two Cities', 'Charles Dickens'), Book(1, 'The Hobbit', 'J.R.R. Tolkien'))"
        """
        book_reprs = ", ".join(repr(book) for book in self.books.values())
        return f"Library({book_reprs})"
    

    def read_book(self, id):
        """Takes in an id of the book read, and
        returns that book's title and the number
        of times it has been read.
        >>> l.read_book(1)
        'The Hobbit has been read 1 time(s)'
        >>> l.read_book(3) # No book with this id
        ''
        """
        if id in self.books:
            book = self.books[id]
            book.times_read += 1
            return book.title + " has been read " + str(book.times_read) + " time(s)"
        else:
            return # no book with this ID

    def read_author(self, author):
        """Takes in the name of an author, and
        returns the total output of reading every
        book written by that author in a single string.
        Hint: Each book output should be on a different line.
        
        >>> l.read_author("Charles Dickens")
        'A Tale of Two Cities has been read 1 time(s)'
        >>> l.read_author("J.R.R. Tolkien")
        'The Hobbit has been read 2 time(s)'
        'The Fellowship of the Ring has been read 1 time(s)'
        """
        # look through all books
        #check book author
        #increment read_count
        output = ""
        for book in self.books.values():
            if book.author == author:
                read_count = self.read_book(book.id)
                if read_count:
                    output += read_count + "\n"
        return output

    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        if book.id not in self.books:
            self.books[book.id] = book
        else:
            return str(book.id) + " is already taken. "

if __name__ == "__main__":
    
    # b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    # b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    # b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    # l = Library(b1, b2, b3)

    #str(l) == 'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'
    #print(str(l))
    #print(l)

    #l.read_book(1) == 'The Hobbit has been read 1 time(s)'
    #print(l.read_book(1))

    #l.add_book(Book(3, "The Sorcerer's Stone", "J.K. Rowling"))
    #print(str(l))

    pass
