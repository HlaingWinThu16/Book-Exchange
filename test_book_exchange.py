import unittest
from book import Book
from user import User
from catalog import Catalog

class TestBookExchangeSystem(unittest.TestCase):

    def setUp(self):
        # Create Users
        self.alice = User("Alice")
        self.bob = User("Bob")

        # Create Books
        self.book1 = Book("1984", "George Orwell", self.alice)
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", self.bob)

        # Create Catalog and add books
        self.catalog = Catalog()
        self.catalog.add_book(self.book1)
        self.catalog.add_book(self.book2)

    def test_book_reservation(self):
        # Alice reserves '1984'
        self.book1.reserve(self.alice)  # Direct call to Book.reserve
        self.assertEqual(self.book1.status, "reserved")
        self.assertEqual(self.book1.reserved_by, self.alice)

    def test_book_double_reservation(self):
        # Alice reserves '1984'
        self.book1.reserve(self.alice)
        # Bob tries to reserve the same book
        with self.assertRaises(Exception) as context:
            self.book1.reserve(self.bob)  # Direct call to Book.reserve
        self.assertTrue("already reserved" in str(context.exception))

    def test_book_release(self):
        # Alice reserves and then releases '1984'
        self.book1.reserve(self.alice)
        self.book1.release()  # Direct call to Book.release
        self.assertEqual(self.book1.status, "available")
        self.assertIsNone(self.book1.reserved_by)

    def test_find_book_by_title(self):
        # Search for a book by title
        found_book = self.catalog.find_book_by_title("1984")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.title, "1984")

    def test_find_nonexistent_book(self):
        # Search for a book that doesn't exist
        found_book = self.catalog.find_book_by_title("Nonexistent Book")
        self.assertIsNone(found_book)

    def test_available_books(self):
        # Alice reserves '1984', so only one book should be available
        self.book1.reserve(self.alice)
        available_books = [book for book in self.catalog.books if book.status == "available"]
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].title, "To Kill a Mockingbird")

if __name__ == '__main__':
    unittest.main()