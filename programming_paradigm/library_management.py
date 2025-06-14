class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        _is_checked_out = False
    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def list_available_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

    def check_out_book(self, book):
        if book in self._books and not book._is_checked_out:
            book._is_checked_out = True
            return True
        return False

    def return_book(self, book):
        if book in self._books and book._is_checked_out:
            book._is_checked_out = False
            return True
        return False