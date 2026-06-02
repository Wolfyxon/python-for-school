"""
Napisz program sortujący tablicę metodą przez wybieranie według zamieszczonej dokumentacji:

Sortowanie przez wybieranie - jedna z prostszych metod sortowania o złożoności O(n2). Polega na
wyszukaniu elementu mającego się znaleźć na żądanej pozycji i zamianie miejscami z tym, który jest tam
obecnie. Operacja jest wykonywana dla wszystkich indeksów sortowanej tablicy.
Algorytm przedstawia się następująco:
1. wyszukaj minimalną wartość z tablicy spośród elementów od i do końca tablicy
2. zamień wartość minimalną, z elementem na pozycji i
Gdy zamiast wartości minimalnej wybierana będzie maksymalna, wówczas tablica będzie posortowana
od największego do najmniejszego elementu.

Założenia do programu
- Program wykonywany w konsoli.
- Obiektowy język programowania zgodny z zainstalowanym na stanowisku egzaminacyjnym: C++ lub
C# lub Java lub Python.
- Sortowanie odbywa się malejąco, nie wykorzystuje gotowych funkcji do sortowania oraz do szukania
maksimum.
- Sortowana jest tablica 10 liczb całkowitych. Tablica jest polem klasy.
- Tablica jest wczytywana z klawiatury po uprzednim wypisaniu odpowiedniego komunikatu.
- Wszystkie elementy posortowanej tablicy są wyświetlane na ekranie.
- Klasa zawiera co najmniej dwie metody: sortującą i szukającą wartość najwyższą. Widzialność
metody szukającej ogranicza się jedynie do klasy.
- Metoda szukająca zwraca wartość, w zależności od przyjętej taktyki może być to wartość
maksymalna lub index wartości maksymalnej.
- Program powinien być zapisany czytelnie, z zasadami czystego formatowania kodu, należy stosować
znaczące nazwy zmiennych i funkcji.
- Dokumentacja do programu wykonana zgodnie z wytycznymi z części III zadania egzaminacyjnego.

"""

class Table:
    """
    /********************************************************
    * nazwa funkcji: __init__
    * parametry wejściowe:
        value - (opcjonalny) Wartość dla tablicy
    * wartość zwracana: brak
    * autor: 1234567890
    * ****************************************************/
    """
    def __init__(self, value = []) -> None:
        self.value = value

    """
    /********************************************************
    * nazwa funkcji: __max_idx
    * parametry wejściowe:
        start - indeks początkowy
    * wartość zwracana:
        int - indeks najwyższej wartości
    * autor: 1234567890
    * ****************************************************/
    """
    def __max_idx(self, start: int = 0) -> int:
        max_i = start

        for i in range(start, len(self.value)): 
            if self.value[i] > self.value[max_i]:
                max_i = i

        return max_i

    """
    /********************************************************
    * nazwa funkcji: sort
    * parametry wejściowe: brak
    * wartość zwracana: brak
    * autor: 1234567890
    * ****************************************************/
    """
    def sort(self) -> None:
        for i in range(len(self.value)):
            min_i = self.__max_idx(i)

            self.value[i], self.value[min_i] = (
                self.value[min_i],
                self.value[i]
            )

    """
    /********************************************************
    * nazwa funkcji: sort
    * parametry wejściowe: brak
    * wartość zwracana: brak
    * autor: 1234567890
    * ****************************************************/
    """
    def print(self) -> None:
        for i in self.value:
            print(i, " ", end = "")
        print()
    
    def load_string(self, string: str) -> None:
        split = string.split(" ")
        self.value = []

        for i in split:
            self.value.append(int(i))

tab = Table()
tab.load_string(input("Podaj elementy tablicy (oddzielone spacją): "))

tab.sort()
print("Posortowana tablica:")
tab.print()
