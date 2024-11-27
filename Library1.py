class Book:
    """
    A class to represent a book in the library.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    isbn (str): The ISBN number of the book.
    is_borrowed (bool): A flag indicating whether the book is currently borrowed.
    borrowed_by (str or None): The user ID of the user who borrowed the book, or None if not borrowed.

    Methods:
    __str__(): Returns a string representation of the book including its title, author, ISBN,
               borrowed status, and the user who borrowed it.
    """
    
    def __init__(self, title, author, isbn):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None  # Tracks the user who borrowed the book

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
        str: A description of the book, including its borrowed status and the user who borrowed it if applicable.
        """
        borrowed_status = f"Yes, by {self.borrowed_by}" if self.is_borrowed else "No"
        return (f"Title: {self.title}, " 
                f"Author: {self.author}, " 
                f"ISBN: {self.isbn}, " 
                f"Borrowed: {borrowed_status}")


class User:
    """
    A class to represent a user in the library system.

    Attributes:
    user_id (str): The unique ID of the user.
    name (str): The name of the user.
    email (str): The email address of the user.

    Methods:
    __str__(): Returns a string representation of the user with their ID, name, and email.
    """
    
    def __init__(self, user_id, name, email):
        """
        Constructs all the necessary attributes for the user object.

        Parameters:
        user_id (str): The unique ID for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        """
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
        str: A description of the user including their ID, name, and email.
        """
        return (f"User ID: {self.user_id}, " 
                f"Name: {self.name}, " 
                f"Email: {self.email}")


class Library:
    """
    A class to represent a library with books and users.

    Attributes:
    books (list): A list of all the books in the library.
    users (dict): A dictionary of users in the library, indexed by their user_id.

    Methods:
    add_book(book): Adds a new book to the library.
    list_books(): Lists all books in the library, or a message if no books exist.
    borrow_book(isbn, user_id): Allows a user to borrow a book by ISBN if available.
    return_book(isbn): Allows a user to return a borrowed book by ISBN.
    add_user(user_id, name, email): Adds a new user to the library system.
    list_users(): Lists all users in the library system, or a message if no users exist.
    update_user(user_id, name=None, email=None): Updates the name and/or email of an existing user.
    delete_user(user_id): Deletes a user from the library system by user_id.
    """
    
    def __init__(self):
        """
        Initializes the library with empty lists for books and users.

        Attributes:
        books (list): An empty list to hold the books in the library.
        users (dict): An empty dictionary to hold the users in the library.
        """
        self.books = []
        self.users = {}  # Store users in a dictionary with their ID as the key

    def add_book(self, book):
        """
        Adds a book to the library.

        Parameters:
        book (Book): A Book object to be added to the library.

        Returns:
        None
        """
        self.books.append(book)
        print(f"Book '{book.title}' added to the library")

    def list_books(self):
        """
        Lists all books in the library. If no books exist, it prints a message indicating so.

        Returns:
        None
        """
        if not self.books:
            print('No books in the Library.')
        for book in self.books:
            print(book)

    def borrow_book(self, isbn, user_id):
        """
        Allows a user to borrow a book by ISBN if the book is available and the user exists.

        Parameters:
        isbn (str): The ISBN number of the book to be borrowed.
        user_id (str): The ID of the user borrowing the book.

        Returns:
        None
        """
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist.")
            return
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = user_id  # Assign the user who borrowed the book
                print(f"User: {self.users[user_id].name} has borrowed '{book.title}'.")
                return
        print("Book not available or does not exist")

    def return_book(self, isbn):
        """
        Allows a user to return a borrowed book by ISBN.

        Parameters:
        isbn (str): The ISBN number of the book being returned.

        Returns:
        None
        """
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                book.borrowed_by = None  # Reset borrowed_by when the book is returned
                print(f"You have returned '{book.title}'.")
                return
        print('Book is not available or has not been borrowed')

    def add_user(self, user_id, name, email):
        """
        Adds a new user to the library system.

        Parameters:
        user_id (str): The unique ID of the user.
        name (str): The name of the user.
        email (str): The email address of the user.

        Returns:
        None
        """
        if user_id in self.users:
            print(f"User ID {user_id} already exists.")
            return
        self.users[user_id] = User(user_id, name, email)
        print(f"User '{name}' added with ID {user_id}.")

    def list_users(self):
        """
        Lists all users in the library system. If no users exist, it prints a message indicating so.

        Returns:
        None
        """
        if not self.users:
            print("No users registered")
            return
        for user in self.users.values():  # Loop through the values in the dictionary
            print(user)

    def update_user(self, user_id, name=None, email=None):
        """
        Updates the details (name and/or email) of an existing user.

        Parameters:
        user_id (str): The ID of the user to be updated.
        name (str, optional): The new name of the user.
        email (str, optional): The new email of the user.

        Returns:
        None
        """
        if user_id not in self.users:
            print("User not found")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User '{user_id}' updated.")

    def delete_user(self, user_id):
        """
        Deletes a user from the library system by user_id.

        Parameters:
        user_id (str): The ID of the user to be deleted.

        Returns:
        None
        """
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted.")
        else:
            print('User not found.')


# Create books
book1 = Book("Think Python: How to Think Like a Computer Scientist", "Allen B. Downey", "9781449332020")
book2 = Book("Automate the Boring Stuff with Python: Practical Programming for Total Beginners", "Al Sweigart", "9781593279929")
book3 = Book("Python for Everybody: Exploring Data in Python 3", "Dr. Charles Russell Severance", "9781530051120")
book4 = Book("The Hitchhiker's Guide to Python: Best Practices for Development", "Kenneth Reitz", "9781491933213")
book5 = Book("Think Stats: Exploratory Data Analysis", "Allen B. Downey", "9781491907344")

# Instantiate the library
library = Library()

# List books in the library (initially empty)
library.list_books()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

print("\nBooks after adding:")
library.list_books()

# Add users
library.add_user("001", "Nidda Rasib", "niddarasib@bradfordcollege.com")
library.add_user("002", "Jane Smith", "janesmith@bradfordcollege.com")
library.add_user("003", "John Doe", "johndoe@bradfordcollege.com")

print("\nUsers after adding:")
library.list_users()

# Borrow books
print("\nBorrowing books:")
library.borrow_book("9781449332020", "001")  # Correct call
library.borrow_book("9781593279929", "002")  # Correct call
library.borrow_book("9781530051120", "003")  # Correct call
library.borrow_book("9781491933213", "003")  # Correct call
library.borrow_book("9781491907344", "001")  # Correct call

# Return books
print("\nReturning books:")
library.return_book("9781449332020")
library.return_book("9781593279929")
library.return_book("9781530051120")
library.return_book("9781491933213")
library.return_book("9781491907344")

# List users after updating
library.update_user("001", name="Nidda Updated", email="updated@bradfordcollege.com")
library.update_user("002", email="newemail@bradfordcollege.com")

print("\nUsers after updates:")
library.list_users()

# Delete a user
library.delete_user("003")
print("\nUsers after deletion:")
library.list_users()

