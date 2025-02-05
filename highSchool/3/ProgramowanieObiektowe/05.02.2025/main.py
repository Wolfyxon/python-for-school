from book import Book
from user import User
from library import Library 

lib = Library()

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
    
    query_main()

def query_main():
    match input("> "):
        case "1":
            register_user()
        case "2":
            add_book()
        case "3":
            pass
        case "4":
            pass
        case "5":
            list_available_books()
        case "6":
            list_users()
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
    print("Wybierz książkę po numerze ISBN")
    
    list_available_books()
    book = get_book_by_isbn()

    if not book: 
        return

    


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