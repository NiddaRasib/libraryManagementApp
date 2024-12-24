
from .book import Book
from .member import StudentMember, TeacherMember
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

        if option == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author name of the book: ")
            isbn = input("Enter the isbn of the book: ")
            library.add_book(Book(title, author, isbn))
            print(f"Book '{title}' added.")


        elif option == "2":
            title = input("Enter the title of the boom you'd like to remove: ")
            library.remove_book(title)
            print(f"Book '{title}' removed.")


        elif option == "3":
            member_type = input("Are you a Student or a Teacher?: ")
            if member_type == "Student" or "student":
                name = input("Enter your full name: ")
                student_id = input("Enter your Student ID: ")
                library.add_member(StudentMember(name, student_id))
                print(f"Student '{name}' added.")

            elif member_type == "Teacher" or "teacher":
                name = input("Enter your full name: ")
                teacher_id = input("Enter your Teacher ID: ")
                library.add_member(TeacherMember(name, teacher_id))
                print(f"Teacher '{name}' added.")

        elif option == "4":
            name = input("Enter the name of the member you'd like to remove: ")
            library.remove_member(name)
            print(f"Member '{name}' removed.")

        
        elif option == "5":
            print("All Books: ")
            library.list_available_books()

        elif option == "6":
            print("All Members: ")
            library.list_members()


        elif option == "7":
            print("Thank you for using our services!")
            break

        else:
            print("Invalid option chosen, please choose an option: ")

