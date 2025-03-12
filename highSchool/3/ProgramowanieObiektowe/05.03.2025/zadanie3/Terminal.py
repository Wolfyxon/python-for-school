from Flight import *
from Passenger import *
from Aircraft import *
from cli import *

class Terminal:
    def __init__(self, flights: list[Flight], passengers: list[Passenger], aircrafts: list[Aircraft]):
        self.flights = flights
        self.passenger = passengers
        self.aircrafts = aircrafts

    def add_flight(self, f: Flight): 
        self.flights.append(f)
        
    def add_passenger(self, p: Passenger):
        self.passengers.append(p)

    def add_aircraft(self, a: Aircraft):
        self.aircrafts.append(a)

    def query_passenger(self) -> Passenger:
        options = []

        for i in self.passengers:
            options.append(Option(str(i), i))

        options.append(Option("< Nowy >", "new"))
        res = query_option(options)

        if not res: 
            return

        if res == "new":
            name1 = input("Podaj imię: ")
            name2 = input("Podaj nazwisko: ")
            doc_id = input_int("Podaj nr dokumentu: ")
            ticket_class = input_int("Podaj klasę biletu: ")

            p = Passenger(name1, name2, doc_id, ticket_class)
            self.add_passenger(p)

            return p
        
        return res