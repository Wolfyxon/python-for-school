from book import Book
from user import User
from library import Library

lib = Library()

lib.books = [
    Book("Pan Tadeusz", "Adam Mickiewicz", 9788307033419),
    Book("Wybór bajek i satyr Krasickiego z oprac. okleina", "Ignacy Krasicki", 9788375178555),
    Book("Felix, Net i Nika oraz Gang Niewidzialnych Ludzi", "Rafał Kosik", 788364384134)
]

def input_int(query: str) -> int:
    try:
        return int(input(query))
    except ValueError:
        print("Nieprawidłowa liczba")
        return input_int(query)

def input_book() -> Book:
    isbn = input_int("(-1 by anulować) > ")

    if isbn == -1:
        return

    book = lib.get_book_by_isbn(isbn)

    if not book:
        print("Nieznana książka")
        return input_book()

    return book

def input_user():
    id = input_int("(-1 by anulować) > ")

    if id == -1:
        return

    user = lib.get_user_by_id(id)

    if not user:
        print("Nieznany użytkownik")
        return input_user()

    return user

def main():
    print("Witaj w bibliotece, co chcesz zrobić?")

    print("1. Zarejestruj użytkownika")
    print("2. Dodaj książkę")
    print("3. Wypożycz książkę")
    print("4. Oddaj książkę")
    print("5. Sprawdź dostępne książki")
    print("6. Wyświetl użytkowników")
    print("7. Zakońćz")

    query_main()

def query_main():
    match input("> "):
        case "1":
            register_user()
        case "2":
            add_book()
        case "3":
            borrow_book()
        case "4":
            return_book()
        case "5":
            list_available_books()
        case "6":
            list_users()
        case "7":
            return
        case _:
            print("Nieznana akcja")
            return query_main()

    main()

def register_user():
    print("Podaj nazwę użytkownika, lub nic by wrócić")

    name = input("> ")

    if name == "":
        return

    user = User(name)
    lib.register_user(user)

    print(f"Użytkownik {name} dodany pomyślnie")

def add_book():
    print("Podaj dane książki")

    title = input("Tytuł: ")
    author = input("Autor: ")
    isbn = input_int("ISBN: ")

    book = Book(title, author, isbn)
    lib.add_book(book)

    print("Książka dodana pomyślnie")

def borrow_book():
    list_available_books()
    print("Wybierz książkę po numerze ISBN")

    book = input_book()

    if not book:
        return

    if not book.available:
        print("Ta książka jest niedostępna")
        return

    list_users()
    print("Wybierz użytkownika, który wypożycza książkę")

    user = input_user()

    if not user:
        return

    user.borrow_book(book)

def return_book():
    list_users()
    print("Wybierz użytkownika")

    user = input_user()

    if not user:
        return

    if len(user.borrowed_books) == 0:
        print("Ten użytkownik nie ma żadnych wypożyczonych książek")
        return

    for i in user.borrowed_books:
        print(i)

    book = input_book()

    if not book:
        return

    if not book in user.borrowed_books:
        print("Użytkownik nie ma tej książki")
        return

    user.return_book(book)

def list_users():
    print("Użytkownicy:")

    for i in range(len(lib.users)):
        print(f"{i} {lib.users[i]}")

    print("")

def list_available_books():
    print("Dostępne książki:")

    books = lib.get_available_books()

    for i in range(len(books)):
        book = books[i]

        print(f"{i}. {book}")

    print("")

main()
