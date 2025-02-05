class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self) -> str:
        return f"{self.author} - {self.title} {self.isbn}"

    def borrow(self):
        assert self.available, "Attempt to borrow an unavailable book"
        self.available = False

    def return_book(self):
        self.available = True
