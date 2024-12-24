
from .book import Book
from .member import Member, StudentMember, TeacherMember
from .library import Library

def main_menu():

    '''
    main menu for user to access the library services

    function allows users to:
    - add or remove books
    - add or remove members
    - view all books and members
    - exit the library system
    '''
    library = Library()

    while True:
        print("Library")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. All Books")
        print("6. All Members")
        print("7. Exit")

        option = input("Choose a number to perform an action: ")

        