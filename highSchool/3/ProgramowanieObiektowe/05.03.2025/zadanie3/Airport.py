from Terminal import Terminal
from Flight import Flight
from Aircraft import Aircraft
from Passenger import Passenger
from cli import *

class Airport:
    def __init__(self, terminals: list[Terminal]):
        self.terminals = terminals

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

    def get_terminal_of_flight(self, flight: Flight) -> Terminal:
        for i in self.terminals:
            if flight in i.flights:
                return i

    def get_terminal_of_passenger(self, passenger: Passenger) -> Terminal:
            for i in self.terminals:
                if passenger in i:
                    return i
    
    def query_terminal(self, required: bool = False) -> Terminal:
        return query_option_str(self.terminals, not required)

    def query_new_passenger(self, terminal: Terminal) -> Passenger:
        name1 = input("Podaj imię: ")
        name2 = input("Podaj nazwisko: ")
        doc_id = input_int("Podaj nr dokumentu: ")
        ticket_class = input_int("Podaj klasę biletu: ")

        p = Passenger(name1, name2, doc_id, ticket_class)
        
        if terminal:
            terminal.add_passenger(p)

        return p

    def query_passenger(self, target_terminal: Terminal = None) -> Passenger:
        options = []

        for i in self.get_passengers():
            options.append(Option(str(i), i))

        options.append(Option("< Nowy >", "new"))
        res = query_option(options)

        if not res:
            return

        if res == "new":
            return self.query_new_passenger(target_terminal)
        
        return res
