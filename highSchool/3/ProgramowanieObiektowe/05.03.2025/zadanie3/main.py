from Airport import *
from Terminal import *
from cli import *


airport = Airport([
    Terminal([], [], [
        Aircraft("Boeing 737", "airbus", 20)
    ]),
    Terminal([], [], [
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