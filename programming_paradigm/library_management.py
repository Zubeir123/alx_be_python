class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book: Book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"'{book.title}' has been checked out.")
                return True
        print(f"'{title}' is not available.")
        return False
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                print(f"'{book.title}' has been returned.")
                return True
        print(f"No such checked out book found: '{title}'")
        return False
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"- {book}")




