class Book:

    def __init__(self, title, author, isbn, year):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year

        super().__init__()

    def __str__(self):
        return self._title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year


class DigitalBook(Book):
    def __init__(self, title, author, isbn, year, size):
        self._file_size = size
        super().__init__(title, author, isbn, year)

class PrintedBook(Book):
    def __init__(self, title, author, isbn, year, edition):
        self._edition = edition
        super().__init__(title, author, isbn, year)

class LibraryIterator:
    def __init__(self, book_list):
        self._book_list = book_list
        self._pos = -1
        super().__init__()

    def __iter__(self):
        return self

    def __next__(self):
        self._pos += 1
        if self._pos < len(self._book_list):
            return self._book_list[self._pos]
        raise StopIteration

class BookTypeIterator:
    def __init__(self, book_list, book_type):
        self._book_list = book_list
        self._book_type = book_type
        self._pos = -1
        super().__init__()

    def __iter__(self):
        return self

    def __next__(self):
        self._pos += 1
        while self._pos < len(self._book_list):
            if isinstance(self._book_list[self._pos], self._book_type):
                return self._book_list[self._pos]
            else:
                self._pos += 1
        raise StopIteration

class BorrowError(Exception):
    def __str__(self):
        return "Problem with borrowing."

class Borrowable:
    def __init__(self, borrowed = False):
        self._borrowed = borrowed

    def borrow(self):
        if self._borrowed:
            raise BorrowError
        self._borrowed = True

    def return_book(self):
        if not self._borrowed:
            raise BorrowError
        self._borrowed = False

    @property
    def is_borrowed(self):
        return self._borrowed


class BorrowablePrintedBook(PrintedBook, Borrowable):
    def __init__(self, title, author, isbn, year, edition):
        super().__init__(title, author, isbn, year, edition)


class Library:

    def __init__(self, books):
        self._books = sorted(books, key=lambda b: b.year)

    def borrow_book(self, title):

        book = next((b for b in self._books if b.title == title and isinstance(b, BorrowablePrintedBook)), None)

        if book:

            try:
                book.borrow()
                return True

            except BorrowError as e:
                print(e)
                return False

    def return_book(self, title):

        book = next((b for b in self._books if b.title == title and isinstance(b, BorrowablePrintedBook)), None)

        if book:

            try:
                book.return_book()
                return True

            except BorrowError as e:
                print(e)
                return False

    def __iter__(self):
        return LibraryIterator(self._books)

    def iterate_by_type(self, book_type):
        return BookTypeIterator(self._books, book_type)

books = [

    PrintedBook(title = "1984", author = "George Orwell", isbn = "9780451524935", year = 1949, edition = 1),
    PrintedBook(title = "To Kill a Mockingbird", author = "Harper Lee", isbn = "9780060935467", year = 1960, edition = 2),
    PrintedBook(title = "Pride and Prejudice", author = "Jane Austen", isbn = "9780141040349", year = 1813, edition = 1),
    PrintedBook(title = "The Great Gatsby", author = "F. Scott Fitzgerald", isbn = "9780743273565", year = 1925, edition = 3),
    PrintedBook(title = "Moby Dick", author = "Herman Melville", isbn = "9781503280786", year = 1851, edition = 2),

    DigitalBook(title = "The Catcher in the Rye", author = "J.D. Salinger", isbn = "9780316769488", year = 1951, size = 1.5),
    DigitalBook(title = "The Hobbit", author = "J.R.R. Tolkien", isbn = "9780261103344", year = 1937, size = 2.3),
    DigitalBook(title = "Harry Potter", author = "J.K. Rowling", isbn = "9780590353427", year = 1997, size = 3.0),
    DigitalBook(title = "1984 (e-book)", author = "George Orwell", isbn = "9780451524935", year = 1949, size = 2.0),
    DigitalBook(title = "Brave New World", author = "Aldous Huxley", isbn = "9780060850524", year = 1932, size = 1.8),

    BorrowablePrintedBook(title = "The Lord of the Rings", author = "J.R.R. Tolkien", isbn = "9780618640157", year = 1954, edition = 1),
    BorrowablePrintedBook(title = "The Road", author = "Cormac McCarthy", isbn = "9780307387899", year = 2006, edition = 2)
]

library = Library(books)

print("All:")
for b in library:
   print(b)

print()
print("Printed:")
for b in library.iterate_by_type(PrintedBook):
   print(b)

print()
print("Digital:")
for b in library.iterate_by_type(DigitalBook):
   print(b)

print()
print("Borrowable:")
for b in library.iterate_by_type(BorrowablePrintedBook):
   print(b)

library.borrow_book("The Lord of the Rings")
library.borrow_book("The Lord of the Rings")
