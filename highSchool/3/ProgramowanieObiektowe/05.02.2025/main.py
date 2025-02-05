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

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(book: Book):
        self.books.append(book)
    
    def register_user(user: User):
        user.user_id = len(self.users)
        self.users.append(user)

    def borrow_book(user_id: int, isbn: int):
        pass

    def return_book(user_id: int, isbn: int):
        pass

    def get_available_books(self) -> list[Book]: # list_available_books()
        res = []

        for i in self.books:
            if i.available:
                res.append(i)

        return res

    def get_user_by_id(self, id: int) -> User:
        return self.users[id]

    def get_book_by_isbn(self, isbn: int) -> Book:
        for i in self.books:
            if i.isbn == isbn:
                return i