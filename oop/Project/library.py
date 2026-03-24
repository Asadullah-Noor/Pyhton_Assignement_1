# 📘 Book Class
class Book:
    def __init__(self, title, author):
        # Store basic info about the book
        self.title = title
        self.author = author
        
        # By default, every new book is available
        self.is_available = True


# 👤 User Class
class User:
    def __init__(self, name):
        # Store user name
        self.name = name
        
        # List to keep track of borrowed books
        self.borrowed_books = []

    def borrow_book(self, book):
        # ❗ Check if user already borrowed 3 books
        if len(self.borrowed_books) >= 3:
            print("❌ Cannot borrow more than 3 books")
            return
        
        # ❗ Check if the book is available
        if book.is_available:
            # Mark book as not available
            book.is_available = False
            
            # Add book to user's borrowed list
            self.borrowed_books.append(book)
            
            print(f"✅ {self.name} borrowed '{book.title}'")
        else:
            print("❌ Book is not available")

    def return_book(self, book):
        # ❗ Check if user actually borrowed this book
        if book in self.borrowed_books:
            # Mark book as available again
            book.is_available = True
            # Remove book from user's list
            self.borrowed_books.remove(book)
            print(f"🔁 {self.name} returned '{book.title}'")
        else:
            print("❌ This book was not borrowed by the user")

    def show_books(self):
        # Display all books borrowed by the user
        print(f"\n📚 {self.name}'s borrowed books:")
        if not self.borrowed_books:
            print("No books borrowed")
        # Loop through borrowed books and print titles
        for book in self.borrowed_books:
            print(f"- {book.title}")
# 🏛️ Library Class
class Library:
    def __init__(self):
        # Store all books in the library
        self.books = []
    def add_book(self, book):
        # Add a new book to library collection
        self.books.append(book)
    def show_all_books(self):
        print("\n📖 Library Books:")
        # Show each book with its availability status
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} by {book.author} → {status}")
# -----------------------------
# 🚀 Testing the system
# -----------------------------
# Create library
lib = Library()
# Create books
b1 = Book("Python Basics", "Ali")
b2 = Book("OOP Concepts", "Sara")
b3 = Book("Data Science", "Ahmed")
b4 = Book("Machine Learning", "Zara")
# Add books to library
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
# Create user
u1 = User("Hamza")
# Borrow books
u1.borrow_book(b1)
u1.borrow_book(b2)
u1.borrow_book(b3)
u1.borrow_book(b4)  # ❌ Should fail (limit reached)
# Show user books
u1.show_books()
# Show library status
lib.show_all_books()
# Return a book
u1.return_book(b2)
# Show updated status
lib.show_all_books()
u1.show_books()