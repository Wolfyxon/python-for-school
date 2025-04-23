class Zwierze:
    def __init__(self, imie: str, wiek: int, gatunek: str):
        self.imie = imie
        self.wiek = wiek
        self.gatunek = gatunek
        
    def przedstaw_sie(self):
        print(f"Cześć! Jestem {self.imie}, mam {self.wiek} lat i jestem {self.gatunek}.")

class Ptak(Zwierze):
    def __init__(self, imie: str, wiek: int, gatunek: str, czy_lata: bool = True):
        super().__init__(imie, wiek, gatunek)
        self.czy_lata = czy_lata

    def latanie(self):
        if self.czy_lata:
            print("Lecę!")
        else:
            print("Nie umiem latać.")

class Ssak(Zwierze):
    def __init__(self, imie: str, wiek: int, gatunek: str, czy_drapieznik: bool = True):
        super().__init__(imie, wiek, gatunek)
        self.czy_drapieznik = czy_drapieznik

    def poluj(self):
        if self.czy_drapieznik:
            print("Poluję na ofiarę!")
        else:
            print("Nie jestem drapieżnikiem.")

orzel = Ptak("ożeu", 4, "Orzeł")
orzel.przedstaw_sie()
orzel.latanie()

tux = Ptak("Tux", 16, "Pingwin", False)
tux.przedstaw_sie()
tux.latanie()

lirili_larila = Ssak("Lirili Larila", 10, "Słoń", False)
lirili_larila.przedstaw_sie()
lirili_larila.poluj()
