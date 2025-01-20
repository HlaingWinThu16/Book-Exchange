class Book:
    def __init__(self, title, author, owner):
        self.title = title
        self.author = author
        self.owner = owner  # The owner is now a User object
        self.status = "available"
        self.reserved_by = None  # Track who has reserved the book
    
    def reserve(self, user):
        """Reserve the book if it's available."""
        if self.status == "available":
            self.status = "reserved"
            self.reserved_by = user  # Track who reserved the book
            print(f"Book '{self.title}' is now reserved by {user.name}.")
        else:
            raise Exception(f"The book '{self.title}' is already reserved.")
    def release(self):
        """Release the book and make it available again."""
        if self.status == "reserved":
            self.status = "available"
            print(f"Book '{self.title}' is now available again.")
            self.reserved_by = None
        else:
            raise Exception(f"The book '{self.title}' is not reserved.")
    
    def __str__(self):
        """Return a string representation of the book's details."""
        return f"'{self.title}' by {self.author} - Owner: {self.owner.name} - Status: {self.status}"
class User:
    def __init__(self, name):
        self.name = name  # The name of the user
    
    def __str__(self):
        return f"User: {self.name}"
    # Create some user instances
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

# Add all books to a list
books = [book1, book2, book3, book4, book5]

# Print the book catalog
print("Book Catalog:")
for book in books:
    print(book)

# Example: Reserving a book
book1.reserve(bob)  # Bob reserves the book '1984'
book2.reserve(charlie)  # Charlie reserves 'To Kill a Mockingbird'

# Print updated catalog after reserving books
print("\nUpdated Book Catalog after Reservations:")
for book in books:
    print(book)
