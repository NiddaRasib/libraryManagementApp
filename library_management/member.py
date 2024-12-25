class Member:
    """
    A class to represent a library member.

    Attributes:
    - name (str): The name of the member.
    - borrowed_books (list): A list of books borrowed by the member.
    """
    def __init__(self, name, member_id):
        """
        Initializes the member with a name, member ID, and an empty list of borrowed books.

        Parameters:
        - name (str): The name of the member.
        - member_id (str): The ID of the member.
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Adds a book to the member's borrowed books list.

        Parameters:
        - book (Book): The book to be borrowed.
        """
        self.borrowed_books.append(book)


    def return_book(self, book):
        """
        Removes a book from the member's borrowed books list.

        Parameters:
        - book (Book): The book to be returned.
        """
        self.borrowed_books.remove(book)


    def list_borrowed_books(self):
        """Returns a list of borrowed book titles."""
        return [book.title for book in self.borrowed_books]


class StudentMember(Member):
    """
    A class to represent a student member, inheriting from Member.

    Attributes:
    - student_id (str): The student ID of the member.
    """
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        


class TeacherMember(Member):
    """
    A class to represent a teacher member, inheriting from Member.

    Attributes:
    - teacher_id (str): The teacher ID of the member.
    """
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)
        
