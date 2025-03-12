from datetime import datetime

class Seat:
    def __init__(self, id: int):
        self.id = id

class Flight:
    def __init__(self, id: int, course: str, departure: datetime, arrival: datetime):
        self.id = id
        self.course = course
        self.departure = departure
        self.arrival = arrival
        self.occupied_seats = []

    def get_seat(self, id: int) -> Seat:
        for i in self.occupied_seats:
            if i.id == id:
                return id

    def get_available_seat_count(self) -> int:
        return self.seat_count - len(self.occupied_seats)