"""
Korzystając z opisu algorytmu sita Eratostenesa, przekształć pseudokod algorytmu do aplikacji konsolowej
szukającej liczb pierwszych w przedziale 2..n, gdzie n = 100.
Ze zbioru liczb naturalnych z przedziału [2, n], tj. {2,3,4,... ,n} wybieramy najmniejszą, czyli 2, i wykreślamy
wszystkie jej wielokrotności większe od niej samej, to jest 4, 6, 8, ... . Z pozostałych liczb wybieramy
najmniejszą niewykreśloną liczbę (3) i wykreślamy wszystkie jej wielokrotności większe od niej samej: 6,
9, 12, ... . Według tej samej procedury postępujemy dla liczby 5. Następnie dla 7 aż do sprawdzenia
wszystkich niewykreślonych wcześniej liczb. Wykreślanie powtarzamy do momentu, gdy liczba i, której
wielokrotność wykreślamy, będzie większa niż √𝑛.

Pseudokod
Niech A będzie tablicą wartości typu logicznego indeksowaną liczbami
całkowitymi od 2 do n (indeksy 0 i 1 nie są brane pod uwagę w czasie
działania algorytmu), początkowo wypełniona wartościami true

for i := 2, 3, 4, ..., nie więcej niż √𝑛:
    if A[i] = true:
        for j := 2*i, 3*i, 4*i, ..., nie więcej niż n :
            A[j] := false

Wyjście: wartości i takie, że A[i] zawiera wartość true.

Założenia programu
- Program wykonywany w konsoli.
- Język programowania zgodny z zainstalowanym na stanowisku egzaminacyjnym, jeden z: C++, C#,
Java, Python.
- Program szuka liczb w przedziale 2..100 (n = 100)
- Wypełnianie tablicy odbywa się w osobnej funkcji przyjmującej tablicę jako argument i nie zwracającej
żadnej wartości.
- Liczby pierwsze są wyświetlane na ekranie, rozdzielone dowolnym separatorem oraz poprzedzone
znaczącym komunikatem.
- Program powinien być zapisany czytelnie, z zachowaniem zasad czystego formatowania kodu, należy
stosować znaczące nazwy zmiennych i funkcji.
- Dokumentacja do programu wykonana zgodnie z wytycznymi z części III zadania egzaminacyjnego.
"""

from math import sqrt

LEN = 100

def fill(array) -> None:
    for i in range(LEN):
        array.append(True)

def sito(array) -> None:
    for i in range(2, int(sqrt(LEN))):
        if array[i]:
            for j in range(2, LEN):
                if i * j >= LEN:
                    break
                array[i * j] = False

array = []

fill(array)
sito(array)

print(f"Liczby pierwsze od 0 do {LEN}:")
for i in range(len(array)):
    if array[i]:
        print(i, end =" ")
print()
