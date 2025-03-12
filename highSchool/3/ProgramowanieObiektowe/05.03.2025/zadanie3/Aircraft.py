class Seat:
    def __init__(self, id: int):
        self.id = id

class Aircraft:
    def __init__(self, registration: str, aircraft_type: str, seat_count: int):
        self.registration = registration
        self.aircraft_type = aircraft_type
        self.seat_count = seat_count
        self.occupied_seats = []

    def get_seat(self, id: int) -> Seat:
        for i in self.occupied_seats:
            if i.id == id:
                return id

    def get_available_seat_count(self) -> int:
        return seat_count - len(self.occupied_seats)