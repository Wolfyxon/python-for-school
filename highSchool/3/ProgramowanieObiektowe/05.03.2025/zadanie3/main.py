from Airport import *
from Terminal import *
from cli import *
from datetime import datetime


airport = Airport([
    Terminal([
        Flight(
            1234, "Warszawa -> Bruksela", 
            datetime(2025, 6, 17, 11, 30), 
            datetime(2025, 6, 17, 18, 40)
        )
    ], [], [
        Aircraft("Boeing 737", "airbus", 20)
    ]),
    Terminal([
            Flight(
            4321, "Warszawa -> Waszyngton", 
            datetime(2025, 4, 5, 15, 00), 
            datetime(2025, 5, 5, 6, 10)
        )
    ], [], [
        Aircraft("Boeing 707", "airbus", 20)
    ])
])

def reserve():
    print("Rezerwacja")

def main():
    print("Witaj w lotnisku")

    main_options = [
        Option("Zarezerwuj bilet", reserve),
    ]

    if not menu(main_options, True):
        return

    main()

main()