from terminal import Terminal
from flight import Flight
from aircraft import Aircraft
from passenger import Passenger

class Airport:
    def __init__(self):
        self.terminals = []

    def get_aircrafts(self) -> list[Aircraft]:
        res = []

        for i in self.terminals:
            res += i.aircrafts

        return res

    def get_flights(self) -> list[Flight]:
        res = []

        for i in self.terminals:
            res += i.flights

        return res

    def get_passengers(self) -> list[Passenger]:
        res = []

        for i in self.terminals:
            res += i.passengers

        return res