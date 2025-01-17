class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track if the book is checked out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"The book '{self.title}' was not checked out.")

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # private list to store book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"The book '{title}' was not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"The book '{title}' was not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available.")
