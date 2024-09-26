import unittest
from library import Book, Library

class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        lib = Library()
        book = Book('123', 'Python 101', 'Author A', 2023)
        lib.add_book(book)
        self.assertIn(book, lib.books)

    def test_borrow_book(self):
        lib = Library()
        book = Book('123', 'Python 101', 'Author A', 2023)
        lib.add_book(book)
        lib.borrow_book('123')
        self.assertFalse(book.is_available)

    def test_borrow_unavailable_book(self):
        lib = Library()
        book = Book('123', 'Python 101', 'Author A', 2023)
        lib.add_book(book)
        lib.borrow_book('123')
        with self.assertRaises(Exception) as context:
            lib.borrow_book('123')
        self.assertEqual(str(context.exception), "Book with ISBN 123 is not available.")

    def test_borrow_nonexistent_book(self):
        lib = Library()
        with self.assertRaises(Exception) as context:
            lib.borrow_book('999')
        self.assertEqual(str(context.exception), "Book with ISBN 999 not found.")

    def test_return_book(self):
        lib = Library()
        book = Book('123', 'Python 101', 'Author A', 2023)
        lib.add_book(book)
        lib.borrow_book('123')
        lib.return_book('123')
        self.assertTrue(book.is_available)

    def test_return_book_not_borrowed(self):
        lib = Library()
        book = Book('123', 'Python 101', 'Author A', 2023)
        lib.add_book(book)
        with self.assertRaises(Exception) as context:
            lib.return_book('123')
        self.assertEqual(str(context.exception), "Book with ISBN 123 was not borrowed.")

    def test_return_nonexistent_book(self):
        lib = Library()
        with self.assertRaises(Exception) as context:
            lib.return_book('999')
        self.assertEqual(str(context.exception), "Book with ISBN 999 not found.")

    def test_view_available_books(self):
        lib = Library()
        book1 = Book('123', 'Python 101', 'Author A', 2023)
        book2 = Book('456', 'Data Science 101', 'Author B', 2022)
        lib.add_book(book1)
        lib.add_book(book2)
        lib.borrow_book('123')
        available_books = lib.view_available_books()
        self.assertIn(book2, available_books)
        self.assertNotIn(book1, available_books)

if __name__ == '__main__':
    unittest.main()
