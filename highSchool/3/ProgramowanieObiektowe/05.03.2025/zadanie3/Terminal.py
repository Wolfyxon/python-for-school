from Flight import *
from Passenger import *
from Aircraft import *

class Terminal:
    def __init__(self, flights: list[Flight], passengers: list[Passenger], aircrafts: list[Aircraft]):
        self.flights = flights
        self.passengers = passengers
        self.aircrafts = aircrafts

    def add_flight(self, f: Flight): 
        self.flights.append(f)
        
    def add_passenger(self, p: Passenger):
        self.passengers.append(p)

    def add_aircraft(self, a: Aircraft):
        self.aircrafts.append(a)
