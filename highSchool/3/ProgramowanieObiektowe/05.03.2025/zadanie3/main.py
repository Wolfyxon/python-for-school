from Airport import *
from Terminal import *
from cli import *


airport = Airport([
    Terminal([], [], []),
    Terminal([], [], [])
])

class ResserveOption(Option):
    def run(self):
        
        pass

def main():
    print("Witaj w lotnisku")

    main_options = [
        ResserveOption("Zarezerwuj bilet"),
    ]

    if not menu(main_options, True):
        return

    main()

main()