from Airport import *
from Terminal import *
from cli import *


airport = Airport([
    Terminal([], [], []),
    Terminal([], [], [])
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