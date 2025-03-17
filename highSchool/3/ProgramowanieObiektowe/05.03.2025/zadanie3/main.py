from Airport import *
from Terminal import *
from cli import *
from datetime import datetime

plane1 = Aircraft("Boeing 737", "airbus", 20)
plane2 = Aircraft("Boeing 707", "airbus", 20)

airport = Airport([
    Terminal([
        Flight(
            1234, "Warszawa -> Bruksela", 
            datetime(2025, 6, 17, 11, 30), 
            datetime(2025, 6, 17, 18, 40),
            plane1
        )
    ], [], [
       plane1
    ]),
    Terminal([
            Flight(
            4321, "Warszawa -> Waszyngton", 
            datetime(2025, 4, 5, 15, 00), 
            datetime(2025, 5, 5, 6, 10),
            plane2
        )
    ], [], [
        plane2
    ])
])

def reserve():

    print("Wybierz lot")
    flight = query_option_str(airport.get_flights(), True)
    term = airport.get_terminal_of_flight(flight)
    if not flight: return

    print("Wybierz pasażera")
    pas = airport.query_passenger(term)
    if not pas: return

    print("Wybierz siedzenie")
    seat = flight.query_reserve_seat()
    if not seat: return
    
    print("Zarezerwowano pomyślnie:")
    print("Pasażer:", pas)
    print("Lot:", flight)
    print("Samolot:", flight.aircraft)

def create_passenger():
    print("Wybierz terminal:")
    t = airport.query_terminal()
    if not t: return

    p = airport.query_new_passenger(t)

    if p:
        print("Pasażer dodany pomyślnie")

def main():
    print("Witaj w lotnisku")

    main_options = [
        Option("Zarezerwuj bilet", reserve),
        Option("Zarejestruj pasażera", create_passenger)
    ]

    if not menu(main_options, True):
        return

    main()

main()