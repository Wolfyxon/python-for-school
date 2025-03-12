class Aircraft:
    def __init__(self, registration: str, aircraft_type: str, seat_count: int):
        self.registration = registration
        self.aircraft_type = aircraft_type
        self.seat_count = seat_count

    def __str__(self) -> str:
        return f"{self.registration} {self.aircraft_type} [{self.seat_count}]"