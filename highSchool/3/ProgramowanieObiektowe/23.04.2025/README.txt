Zadanie: "Zwierzęcy Świat"
W pewnym wirtualnym zoo mamy różne zwierzęta. Każde z nich ma pewne wspólne cechy, ale też własne, charakterystyczne zachowania. 
Twoim zadaniem jest zaimplementować hierarchię klas przy użyciu dziedziczenia w języku Python.Wymagania:Stwórz klasę bazową Zwierze, która będzie posiadać:
    atrybuty: imie, wiek, gatunek
    metodę przedstaw_sie(), która wypisze informacje o zwierzęciu w stylu:
    "Cześć! Jestem [imię], mam [wiek] lat i jestem [gatunek]."
Stwórz klasy pochodne:
    Ptak:
        dodatkowy atrybut: czy_lata (bool)
        metoda latanie(), która wypisze "Lecę!" jeśli czy_lata=True, w przeciwnym razie "Nie umiem latać."
    Ssaki:
        dodatkowy atrybut: czy_drapieżnik (bool)
        metoda poluj(), która wypisze "Poluję na ofiarę!" jeśli czy_drapieżnik=True, w przeciwnym razie "Nie jestem drapieżnikiem."
        Utwórz po jednym obiekcie z każdej klasy pochodnej i przetestuj działanie metod.

Przykład użycia:

orzel = Ptak("Orzeł", 5, "ptak drapieżny", True) 
orzel.przedstaw_sie() 
orzel.latanie() 

 krowa = Ssaki("Mućka", 3, "krowa", False) 
krowa.przedstaw_sie() 
krowa.poluj()