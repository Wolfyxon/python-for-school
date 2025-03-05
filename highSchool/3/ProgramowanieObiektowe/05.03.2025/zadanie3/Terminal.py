from Flight import *
from Passenger import *
from Aircraft import *

class Terminal:
    def __init__(self):
        self.flights = []
        self.passenger = []
        self.aircrafts = []

    def add_flight(self, f: Flight): 
        self.flights.append(f)
        
    def add_passenger(self, p: Passenger):
        self.passengers.append(p)

    def add_aircraft(self, a: Aircraft):
        self.aircrafts.append(a)