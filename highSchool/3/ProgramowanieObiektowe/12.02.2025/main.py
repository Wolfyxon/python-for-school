class Movie:
    def __init__(self, title: str, tickets: int, ticket_cost: int):
        self.title = title
        self.available_tickets = tickets
        self.total_tickets = tickets
        self.ticket_cost = ticket_cost

    def __str__(self) -> str:
        return f"{self.title} ({self.available_tickets} / {self.total_tickets}) {self.ticket_cost} zł"

    def zarezerwuj_miejsce(self):
        assert self.available_tickets > 0, "Sold out"

        self.available_tickets -= 1

class User:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.name} ({self.balance} zł)"

    def kup_bilet(self, movie: Movie):
        if movie.available_tickets <= 0:
            print("Bilety wyprzedane")
            return
        
        if self.balance < movie.ticket_cost:
            print("Brak wystarczających środków")
            return

        movie.zarezerwuj_miejsce()
        self.balance -= movie.ticket_cost

users = [
    User("Mr Majonez", 999),
    User("Friderick von Fazbear", 87),
    User("Jan", 2)
]

movies = [
    Movie("Incenpcja", 10, 30),
    Movie("Kopaćrzemiosło Film", 2, 35),
    Movie("Ryba", 17, 17)
]

def print_list(ls: list):
    for i in range(len(ls)):
        print(f" {i + 1}. {ls[i]}")

def query_list_menu(ls: list):
    print_list(ls)
    
    return query_list(ls)

def query_list(ls: list):
    try:
        idx = int(input("(-1 by anulować) > "))

        if idx == -1: 
            return

        if len(movies) < idx or idx <= 0:
            print("Nieznany")
            return query_list(ls)

        return ls[idx - 1]

    except ValueError:
        print("Niepoprawna liczba")
        return query_list(ls)

def query_user() -> User:
    return query_list_menu(users)

def query_movie() -> Movie:
    return query_list_menu(movies)

def main():
    print("Witaj w kinie")
    print("Co chcesz zrobić?")
    
    print("1. Kup bilet")
    print("2. Wyświetl filmy")
    print("3. Wyświetl urzytkowników")
    print("4. Wyjdź")

    query_main()

def query_main():
    match input("> "):
        case "1":
            buy()
        case "2":
            print_list(movies)
        case "3":
            print_list(users)
        case "4":
            return

    main()

def buy():
    print("Wybierz film:")

    movie = query_movie()
    if not movie: return

    print("Wybierz użytkownika:")

    user = query_user()
    if not user: return

    user.kup_bilet(movie)

main()