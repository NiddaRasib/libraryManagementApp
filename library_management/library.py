import json
from .book import Book
from .member import Member, StudentMember, TeacherMember

class Library:
    """
    Represents a library.

    Attributes:
    - books (list): A list of books in the library.
    - members (list): A list of members in the library.
    """

    def __init__(self):
        """
        Initializes an empty library.
        """
        self.books = [] # empty list to store books
        self.members = [] # empty list to store members of the library

    def add_book(self, book):
        """
        Adds a book to the library.
        """
        self.books.append(book)  
        

    def remove_book(self, title):
        """
        Removes a book from the library.
        """
        self.books = [book for book in self.books if book.title != title]


    def add_member(self, member):
        """
        Adds a member to the library.
        """
        self.members.append(member)
        

    def remove_member(self, name):
        """
        Removes a member from the library.
        """
        self.members = [member for member in self.members if member.name != name]
        

    def list_borrowed_book(self, book, member):
        """
        Allows a member to borrow a book from the library.

        Args:
        - book (Book): The book to be borrowed.
        - member (Member): The member borrowing the book.
        """
        for member in self.members:
            for book in member.borrow_books:
                print(f"Title: {book.title}, Borrowed by: {member.name}")
        

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


    def borrow_book(self, member_name, book_title):
        """
        Lists all borrowed books and their borrowers.
        """
        member = None
        for m in self.members:
            if m.name == member_name:
                member = m
                break

        book = None
        for b in self.books:
            if b.title == book_title and not b.is_borrowed:
                book = b
                break

        for member in self.members:
            for book in member.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Borrower: {member.name}")

    
    def return_book(self, book_title, member_name):
        """
        Allows a member to return a book to the library.

        Args:
        - book (Book): The book to be returned.
        - member (Member): The member returning the book.
        """

        member = None
        for m in self.members:
            if m.name == member_name:
                member = m
                break

        book = None
        for b in self.books:
            if b.title == book_title and not b.is_borrowed:
                book = b
                break


        self.books.append(book)
        member.return_book(book)