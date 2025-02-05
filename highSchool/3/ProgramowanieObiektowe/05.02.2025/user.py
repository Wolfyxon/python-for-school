from book import Book

class User:
    def __init__(self, name: str):
        self.name = name
        self.user_id = -1
        self.borrowed_books = []

    def __str__(self) -> str:
        return f"{self.name} ({self.user_id})"

    def borrow_book(book: Book):
        self.borrowed_books.append(book)
        book.borrow()

    def return_book(book: Book):
        self.borrowed_books.remove(book)
        book.return_book()
