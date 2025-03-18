from datetime import datetime
from Aircraft import *
from Passenger import *
from cli import *

class Seat:
    def __init__(self, id: int, passenger: Passenger):
        self.id = id
        self.passenger = passenger

class Flight:
    def __init__(self, id: int, course: str, departure: datetime, arrival: datetime, aircraft: Aircraft):
        self.id = id
        self.course = course
        self.departure = departure
        self.arrival = arrival
        self.aircraft = aircraft

        self.occupied_seats = []

    def __str__(self) -> str:
        return f"{self.course} | {self.id} {self.departure} -> {self.arrival}"

    def get_seat(self, id: int) -> Seat:
        for i in self.occupied_seats:
            if i.id == id:
                return id

    def get_available_seat_count(self) -> int:
        return self.aircraft.seat_count - len(self.occupied_seats)

    def print_seats(self):
        seat_count = self.aircraft.seat_count
        max_ln = len(str(seat_count))

        menu = ""

        for i in range(seat_count):
            if i % 10 == 0:
                menu += "\n"

            if self.get_seat(i):
                menu += f"[{" " * max_ln}]"
            else:
                menu += f"[{i + 1}{" " * (max_ln - len(str(i)))}]"

        print(menu)

    def reserve_seat(self, passenger: Passenger, seat_id: int) -> Seat:
        seat = Seat(seat_id, passenger)
        self.occupied_seats.append(seat)

        return seat

    def query_reserve_seat(self, passenger: Passenger, show_menu: bool = True) -> Seat:
        seat_count = self.aircraft.seat_count
        
        if show_menu:
            print("Dostępne miejsca:")
            self.print_seats()
            print("Wybierz miejsce lub wpisz -1 by anulować:")

        sid = input_int("> ") - 1

        if sid == -1:
            return False

        if sid < 0 or sid > seat_count:
            print("Niepoprawny numer miejsca")
            return self.query_reserve_seat(False)

        if self.get_seat(sid):
            print("To miejsce jest zajęte")
            return self.query_reserve_seat(False)

        return self.reserve_seat(passenger, sid)

        