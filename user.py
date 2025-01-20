# Import the Book class if it's in another file
from book import Book

class User:
    def __init__(self, name):
        self.name = name  # The name of the user
    
    def __str__(self):
        return f"User: {self.name}"

    def reserve_book(self, book):
        """Reserve a book if it's available."""
        if book.status == "available":  # Ensure the book is available before reserving
            book.reserve(self)  # Call reserve method from Book class with the current user
    
    def release_book(self, book):
        """Release a book and make it available again."""
        book.release()  # Release the book using the current user