from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)
    
    def register_user(self, user: User):
        user.user_id = len(self.users)
        self.users.append(user)

    def borrow_book(self, user_id: int, isbn: int):
        pass

    def return_book(self, user_id: int, isbn: int):
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