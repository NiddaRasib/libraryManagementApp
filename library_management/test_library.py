'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

def create_instance():
    # Create a new instance of the Book class
    try:
        book = Book("Fluent Python", "Luciano Ramalho")
        print("New instance of Book class created", book)
    except NameError as e:
        print(e)

    # Create a new instance of the Library class
    try:
        library = Library()
        if isinstance(library, Library):
            print("Library instance created")
    except NameError as e:
        print(e)

    # Create a new instance of the Member class
    try:
        member = Member("Ezra Sherman", "48762")
        print("New instance of member class created", member)
    except NameError as e:
        print(e)



'''
Library Operations
'''

# Add books to the library
library = Library()
book = Book("Fluent Python", "Luciano Ramalho", "9781491946268")
library.add_book(book)
print("Book was added to the library")


# Add member to the library
library = Library()
member = StudentMember("Ricardo Kane", "29740")
library.add_member(member)
print("student member was added to the library")


# List available books in the library
library = Library()
book = Book("Fluent Python", "Luciano Ramalho", "9781491946268")
library.add_book(book)
list_available_books 

# Borrow a book from the library
library = Library()
book = Book("Fluent Python", "Luciano Ramalho", "9781491946268")
library.add_book(book)


# List borrowed books from the library

