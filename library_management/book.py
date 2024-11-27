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
        return (f"Title: {self.title}", 
                f"Author: {self.author}", 
                f"ISBN: {self.isbn}")

        