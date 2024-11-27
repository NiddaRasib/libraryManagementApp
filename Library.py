class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author, isbn):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        borrowed_status = f"Yes, by {self.borrowed_by}" if self.is_borrowed else "No"
        return (f"Title: {self.title}, " 
                f"Author: {self.author}, " 
                f"ISBN: {self.isbn}, " 
                f"Borrowed: {'Yes' if self.is_borrowed else 'No'}")
    
class User:
    """
    A class to represent a user.

    Attributes:
    user_id (str): The unique ID of the user.
    name (str): The name of the user.
    email (str): The email address of the user.
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


    def __str__(self):
        return (f"User ID: {self.user_id}, " 
                f"Name: {self.name}, " 
                f"Email: {self.email}")
    

class Library:
    """
    A class to represent a library.
    """

    def __init__(self):
        self.books = []
        self.users = {}  # Store users in a dictionary with their ID as the key

    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library")

    
    def list_books(self):
        if not self.books:
            print('No books in the Library.')
        for book in self.books:
            print(book)

    
    def borrow_book(self, isbn, user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist.")
            return
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = user_id  # Now correctly assign the user_id to the borrowed_by attribute
                print(f"User: {self.users[user_id].name} has borrowed '{book.title}'.")
                return
        print("Book not available or does not exist")


    #def borrow_book(self, isbn):
        #for book in self.books:
            #if book.isbn == isbn and not book.is_borrowed:
                #book.is_borrowed = True
                #print(f"You have borrowed: '{book.title}'.")
                #return
        #print('Book is not available or has been borrowed')

    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                book.borrowed_by = None
                print(f"You have returned '{book.title}'. ")
                return
            print('Book is not available or has not been borrowed')


    def add_user(self, user_id, name, email):
        if user_id in self.users:
            print(f"User ID {user_id} already exists.")
            return
        self.users[user_id] = User(user_id, name, email)
        print(f"User '{name}' added with ID {user_id}.")


    def list_users(self):
        if not self.users:
            print("No users registered")
            return
        for user in self.users.values(): # Loop through the values in the dictionary
            print(user)  # Now 'user' is defined as the User object


    def update_user(self, user_id, name=None, email=None):
        if user_id not in self.users:
            print("User not found")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User '{user_id}' updated.")


    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted.")
        else:
            print('User not found.')

        
 
book1 = Book("Think Python: How to Think Like a Computer Scientist", "Allen B. Downey", "9781449332020")
book2 = Book("Automate the Boring Stuff with Python: Practical Programming for Total Beginners", "Al Sweigart", "9781593279929")
book3 = Book("Python for Everybody: Exploring Data in Python 3", "Dr. Charles Russell Severance", "9781530051120")
book4 = Book("The Hitchhiker's Guide to Python: Best Practices for Development", "Kenneth Reitz", "9781491933213")

print(book1)
print(book3)

print()

# instantiate the library
library = Library()


# List books in the library (initially empty)
library.list_books()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.add_book(Book("Think Stats: Exploratory Data Analysis", "Allen B. Downey", "9781491907344"))

print("\nBooks after adding:")

# List books after adding them
library.list_books()

print()

# Borrow books
print("\nBorrowing books:")
library.borrow_book("9781449332020", "001")  
library.borrow_book("9781593279929", "002")  
library.borrow_book("9781530051120", "003")  
library.borrow_book("9781491933213", "004") 
#library.borrow_book("9781420") # not associated with any books

print()

# Return books
library.return_book("9781449332020")
library.return_book("9781593279929")
library.return_book("9781530051120")
library.return_book("9781491933213")
library.return_book("9781420") # not associated with any books

print(book4)

# Add users
library.add_user("001", "Nidda Rasib", "niddarasib@bradfordcollege.com")
library.add_user("002", "Jane Smith", "janesmith@bradfordcollege.com")

print("\nUsers after adding:")

library.list_users()

print()

# Update users
library.update_user("001", name="Nidda Rasib", email="update@bradfordcollege.com")
library.update_user("002",  email="janesmith1234@bradfordcollege.com")
library.update_user("003",  email="Thames1234@bradfordcollege.com")

print()

library.list_users()

print()

# Delete user 001
library.delete_user('001')

print()

library.list_users()




