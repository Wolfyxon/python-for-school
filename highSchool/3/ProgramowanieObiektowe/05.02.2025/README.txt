Stwórz program symulujący system zarządzania biblioteką. System powinien umożliwiać:  
1. Dodawanie książek do katalogu.  
2. Rejestrowanie użytkowników biblioteki.  
3. Wypożyczanie i zwracanie książek przez użytkowników.  
4. Sprawdzanie dostępności książek.  

Wymagania:
- **Klasa `Book`**  
  - Atrybuty: `title`, `author`, `isbn`, `available` (czy książka jest dostępna).  
  - Metody: `borrow()`, `return_book()`, `__str__()`.  

- **Klasa `User`**  
  - Atrybuty: `name`, `user_id`, `borrowed_books` (lista wypożyczonych książek).  
  - Metody: `borrow_book(book)`, `return_book(book)`, `__str__()`.  

- **Klasa `Library`**  
  - Atrybuty: `books` (lista wszystkich książek), `users` (lista użytkowników).  
  - Metody: `add_book(book)`, `register_user(user)`, `borrow_book(user_id, isbn)`, `return_book(user_id, isbn)`, `list_available_books()`.