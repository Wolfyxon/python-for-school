"""
Zaprogramuj klasę o nazwie Kosc implementującą logikę działania pojedynczej kości, wykorzystywanej
później w grze w kości. Każda ściana kości zawiera unikatową liczbę oczek równą wartości wyrzuconej z
zakresu 1 ÷ 6.
Założenia do programu:
‒ Wykonywany w konsoli
‒ Zastosowany obiektowy język programowania zgodny z zainstalowanym na stanowisku
egzaminacyjnym: C++ lub C#, lub Java, lub Python
‒ Zastosowane znaczące, angielskie lub polskie nazewnictwo zmiennych i funkcji
‒ Zapisany czytelnie, z zachowaniem zasad czystego formatowania kodu
Klasa Kosc powinna zawierać:
‒ Pole ogólnodostępne, statyczne, przechowujące liczbę instancji klasy Kosc
‒ Pola ogólnodostępne, przechowujące:
‒ Nazwy plików przechowujących obrazy (kosc0.png, kosc1.png, kosc2.png, kosc3.png,
kosc4.png, kosc5.png, kosc6.png) umieszczone w tablicy lub innej kolekcji typu
napisowego
‒ Liczba oczek wyrzucona kością, typu liczbowego całkowitego (3 dla obrazu 1)
‒ Identyfikator pliku graficznego odpowiadającego wyrzuconej liczbie oczek, typu całkowitego (3 dla
obrazu 1, jest to indeks tablicy wskazujący na nazwę kosc3.png)
‒ Informacja czy kość jest dostępna, typu logicznego
‒ Konstruktory klasy:
‒ Jednoargumentowy, którego argument jest wartością wyrzuconej kości.
‒ W przypadku, gdy wartość argumentu jest inna niż 1, 2, 3, 4, 5 lub 6, ustawia wartość na 0.
‒ Przypisuje liczbie oczek i identyfikatorowi pliku wartość argumentu
‒ Przypisuje wartość polu logicznemu: kość jest dostępna
‒ Inkrementuje zmienną statyczną zliczającą instancje klasy
‒ Bezargumentowy:
‒ Losuje liczbę pseudolosową z zakresu od 1 do 6
‒ Przypisuje liczbie oczek i identyfikatorowi pliku wylosowaną liczbę
‒ Przypisuje wartość polu logicznemu: kość jest dostępna
‒ Inkrementuje zmienną statyczną zliczającą instancje klasy
‒ Metoda ogólnodostępna, bezparametrowa, niezwracająca wartości, która realizuje rzut kością tylko, gdy
kość jest dostępna:
‒ Losuje wartość z zakresu od 1 do 6
‒ Przypisuje wylosowaną wartość do pola liczby oczek i identyfikatora pliku graficznego
‒ Metoda ogólnodostępna, bezparametrowa, niezwracająca wartości, która blokuje kość:
‒ Ustawiana jest informacja, że kość jest niedostępna
‒ Metoda ogólnodostępna, bezparametrowa, zwracająca wartość wyrzuconą na kości w postaci tekstu
(np. gdy wartość jest równa 3, zwracane jest „trzy”)
Sprawdź działanie klasy w programie głównym:
‒ Należy utworzyć dwa obiekty klasy Kosc, każdy za pomocą innego konstruktora
‒ W przypadku konstruktora jednoargumentowego liczba przekazana jako argument ma być pobrana
z klawiatury
‒ Po utworzeniu każdego obiektu należy wyświetlić:
o Liczbę utworzonych instancji klasy
o Informację o liczbie oczek wyrzuconych kością (w postaci liczbowej i napisowej)
o Nazwę pliku odpowiadającego wyrzuconej liczbie oczek
‒ Informacja powinna być zrozumiała dla użytkownika


Uwaga: W języku Python należy utworzyć jeden konstruktor z domyślną wartością argumentu None
"""

import random
import unittest

class Kosc:
    instances = 0

    def __init__(self, value = None) -> None:
        if value == None:
            self.value = random.randint(1, 6)
        else:
            if value < 1 or value > 6:
                self.value = 0
            else:
                self.value = value

        # This is so inefficient

        self.file_names = ["kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
        self.available = True
        self.file_idx = self.value
        Kosc.instances += 1

    def block(self) -> None:
        self.available = False

    def throw(self) -> None:
        if not self.available:
            return

        self.value = random.randint(1, 6)
        self.file_idx = self.value

    def value_string(self) -> str:
        names = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć"]

        return names[self.value]

class TestKosc(unittest.TestCase):
    def test_throw(self) -> None:
        k = Kosc()
        k.throw()
        self.assertTrue(k.value > 0 and k.value <= 6)

    def test_blocked(self) -> None:
        init_v = 4
        k = Kosc(init_v)
        
        k.block()
        k.throw()

        self.assertEqual(k.value, init_v)

def print_info(last_die: Kosc) -> None:
    print(f"Instancje Kosc: {Kosc.instances}")
    print(f"Liczba oczek: {last_die.value} ({last_die.value_string()})")
    print(f"Nazwa pliku obrazu: {last_die.file_names[last_die.file_idx]}")
    print()

def main() -> None:
    unittest.main()

    print("Kość A")
    kosc_a = Kosc()
    print_info(kosc_a)

    b_value = int(input("Podaj wartość dlam kości B: "))
    print()

    print("Kość B")
    kosc_b = Kosc(b_value)
    print_info(kosc_b)

main()