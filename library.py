class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True  # Book is available by default


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library"""
        self.books.append(book)

    def borrow_book(self, isbn):
        """Allows a user to borrow a book if it's available"""
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    return book
                else:
                    raise Exception(f"Book with ISBN {isbn} is not available.")
        raise Exception(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        """Allows a user to return a borrowed book"""
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.is_available = True
                    return
                else:
                    raise Exception(f"Book with ISBN {isbn} was not borrowed.")
        raise Exception(f"Book with ISBN {isbn} not found.")

    def view_available_books(self):
        """Returns a list of all available books in the library"""
        return [book for book in self.books if book.is_available]
