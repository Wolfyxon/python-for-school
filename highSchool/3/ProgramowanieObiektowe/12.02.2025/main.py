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