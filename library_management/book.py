class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    isbn (str): The isbn of the book.
    """

    def __init__(self, title, author, isbn):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The isbn of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        

    def __str__(self):
        """
        returns a string for the book object.

        string contains the:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The isbn of the book.
        """
        return (f"Title: {self.title}", 
                f"Author: {self.author}", 
                f"ISBN: {self.isbn}")
    

title = input("Enter the title of the book: ")
author = input("Enter the author name of the book: ")
isbn = input("Enter the isbn of the book: ")

book = Book(title, author, isbn)

print(book)



        