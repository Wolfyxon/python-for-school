class Movie:
    def __init__(self, title: str, tickets: int, ticket_cost: int):
        self.title = title
        self.available_tickets = tickets
        self.total_tickets = tickets
        self.ticket_cost = ticket_cost

class User:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    