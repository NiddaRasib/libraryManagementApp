
from book import Book
from member import StudentMember, TeacherMember
from library import Library


def main_menu():
    '''
    main menu for user navigation
    '''

    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Books")
        print("2. Members")
        print("3. Exit")

        option = input("\nChoose an option: ")
        if option == "1": #Books
            book_menu(library)
        elif option == "2": #Members
            member_menu(library)
        elif option == "3": #Exit the system
            print("\nThank you for using Bradford College Library System!")
            break
        else:
            print("Invalid option please try again")




def book_menu(library):

    '''
    book menu for user navigation
    '''

    while True:
        print("\nBook Management Menu")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List all available books")
        print("6. List borrowed books")
        print("7. Return to main menu")

        option = input("Choose an option: ")

        if option == "1": #adding a book
            title = input("Enter the title of the book: ")
            author = input("Enter the author name of the book: ")
            isbn = input("Enter the isbn of the book: ")
            library.add_book(Book(title, author, isbn))
            print(f"Book '{title}' added.")


        elif option == "2": #deleting a book
            title = input("Enter the title of the boom you'd like to remove: ")
            library.remove_book(title)
            print(f"Book '{title}' removed.")
        

        elif option == "3": #borrow a book
            member_name = input("Enter your member name: ")
            book_title = input("Enter the title of the book youd like to borrow: ")
            library.borrow_book(member_name, book_title)


        elif option == "4": #return a book
            member_name = input("Enter your member name: ")
            book_title = input("Enter the title of the book you are returning: ")
            library.return_book(member_name, book_title)


        elif option == "5": #listing all books
            print("\nAvailable books: ")
            library.list_available_books()


        elif option == "6": #listing all the users borrowed books
            print("\nBorrowed Books: ")
            library.list_borrowed_books()


        elif option == "7": #return back to main menu
            print("\nReturning back to main menu")
            break
        else:
            print("Invalid option please try again")



def member_menu(library):

    '''
    member menu for user navigation
    '''

    while True:
        print("\nMember Management Menu")
        print("1. Add a member")
        print("2. Delete a member")
        print("3. List all members")
        print("4. Return to main menu")

        option = input("\nChoose an option: ")

        if option == "1": #add a member
            member_type = input("\nAre you a Student or a Teacher?: ").lower()
            name = input("Enter your full name: ")
            member_id = input("Enter your ID number: ")

            if member_type == "student":
                member = StudentMember(name, member_id)
            elif member_type == "teacher":
                member = TeacherMember(name, member_id)
            else:
                print("\nInvalid member type please try again")
                continue
            library.add_member(member)
            print(f"'{name}' added.")


        elif option == "2": #delete a member
            name = input("\nEnter the name of the member you'd like to remove: ")
            library.remove_member(name)
            print(f"Member '{name}' removed.")


        elif option == "3": #list all library members
            print("All Members: ")
            library.list_members()


        elif option == "4": #return back to main menu
            print("\nReturning back to main menu")
            break
        else:
            print("\nInvalid option please try again")

if __name__ == "__main__":
    main_menu()
