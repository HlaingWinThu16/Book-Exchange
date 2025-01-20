# Import necessary classes
from catalog import Catalog
from book import Book
from user import User

# Create a catalog to manage books
catalog = Catalog()

# Create user instances
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")
diana = User("Diana")
eve = User("Eve")
# Create book instances and associate them with the users
book1 = Book("1984", "George Orwell", alice)
book2 = Book("To Kill a Mockingbird", "Harper Lee", bob)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", charlie)
book4 = Book("Pride and Prejudice", "Jane Austen", diana)
book5 = Book("Moby Dick", "Herman Melville", eve)

# Add books to the catalog
catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)
catalog.add_book(book4)
catalog.add_book(book5)
# Show the entire catalog
catalog.show_catalog()

# Show available books
catalog.available_books()

# Example: Alice reserves a book
book_to_reserve = catalog.find_book_by_title("1984")
if book_to_reserve:
    alice.reserve_book(book_to_reserve)  # Alice reserves '1984'

# Show available books after reservation
catalog.available_books()
# Example: Bob reserves a book
book_to_reserve = catalog.find_book_by_title("The Great Gatsby")
if book_to_reserve:
    bob.reserve_book(book_to_reserve)  # Bob reserves 'The Great Gatsby'

# Show available books after another reservation
catalog.available_books()

# Example: Alice releases a book
alice.release_book(book1)  # Alice releases '1984'

# Show the catalog after releasing the book
catalog.show_catalog()