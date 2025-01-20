class Catalog:
    def __init__(self):
        self.books = []  # List to store all books
    
    def add_book(self, book):
        """Add a book to the catalog."""
        self.books.append(book)
    
    def show_catalog(self):
        """Display the catalog of books."""
        print("\nBook Catalog:")
        for book in self.books:
            print(book)
    
    def available_books(self):
        """Display only available books."""
        print("\nAvailable Books:")
        for book in self.books:
            if book.status == "available":
                print(book)
    def find_book_by_title(self, title):
        """Find a book in the catalog by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None