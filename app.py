from flask import Flask, render_template, request, jsonify
from catalog import Catalog
from book import Book
from user import User

app = Flask(__name__)

# Set up the catalog
catalog = Catalog()
catalog.add_book(Book("1984", "George Orwell", User("Alice")))
catalog.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", User("Bob")))
catalog.add_book(Book("To Kill a Mockingbird", "Harper Lee", User("Charlie")))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_books', methods=['GET'])
def get_books():
    books = [{"title": book.title, "author": book.author, "owner": book.owner.name, "status": book.status} for book in catalog.books]
    return jsonify(books)

@app.route('/reserve_book', methods=['POST'])
def reserve_book():
    data = request.json
    title = data.get("title")
    user_name = data.get("user")
    user = User(user_name)
    book = catalog.find_book_by_title(title)
    if book:
        try:
            user.reserve_book(book)
            return jsonify({"message": f"Book '{title}' reserved successfully."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Book not found."}), 404

@app.route('/release_book', methods=['POST'])
def release_book():
    data = request.json
    title = data.get("title")
    user_name = data.get("user")
    user = User(user_name)
    book = catalog.find_book_by_title(title)
    if book:
        try:
            user.release_book(book)
            return jsonify({"message": f"Book '{title}' released successfully."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Book not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)