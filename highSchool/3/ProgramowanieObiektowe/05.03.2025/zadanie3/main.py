from Airport import Airport
from cli import *

airport = Airport()

class ResserveOption(Option):
    def run(self):
        
        pass

def main():
    print("Witaj w lotnisku")

    menu([
        ResserveOption("Zarezerwuj bilet")
    ])

main()