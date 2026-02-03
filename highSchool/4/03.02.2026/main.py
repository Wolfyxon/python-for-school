from math import sqrt, ceil

"""
*******************************************************
nazwa funkcji: fill_array
parametry wejściowe: array  - tablica
                     length - oczekiwana długość tablicy
wartość zwracana: brak
informacje: Wypełnia tablicę wartościami True
autor: 1234567890
****************************************************
"""
def fill_array(array, length):
    for i in range(length):
        array.append(True)


"""
*******************************************************
nazwa funkcji: process_array
parametry wejściowe: array - tablica wartości boolean
wartość zwracana: brak
informacje: Wykonuje sito Eratostenesa na podanej tablicy
autor: 1234567890
****************************************************
"""
def process_array(array):
    num_count = len(array)

    for i in range(2, ceil(sqrt(num_count))):
        if array[i]:
            for j in range(2 * i, num_count, i):
                array[j] = False

"""
*******************************************************
nazwa funkcji: print_bool_array
parametry wejściowe: array - tablica wartości boolean
wartość zwracana: brak
informacje: Wyświetla liczby dla wartości True w tablicy
autor: 1234567890
****************************************************
"""
def print_bool_array(array):
    for i in range(2, len(array)):
        if array[i]:
            print(i, end=", ")
    
    print()

"""
*******************************************************
nazwa funkcji: bool_array_to_numbers
parametry wejściowe: array - tablica wartości
wartość zwracana: list[int] - Tablica liczb
informacje: Konwertuje tablicę wartości boolean na 
            liczby dla każdej wartości True
autor: 1234567890
****************************************************
"""
def bool_array_to_numbers(array):
    res = []

    for i in range(2, len(array)):
        if array[i]:
            res.append(i)

    return res


"""
*******************************************************
nazwa funkcji: test_array
parametry wejściowe: length - długość tablicy do wygenerowania
                     expected - oczekiwane liczby
wartość zwracana: brak
informacje: Generuje tablicę wartości boolean o
            podanej długości, po czym uruchamia
            process_array() i porównuje wynik
            z oczekiwanym.
autor: 1234567890
****************************************************
"""
def test_array(length, expected):
    array = []
    fill_array(array, length)
    process_array(array)

    assert bool_array_to_numbers(array) == expected, f"Zwrócono {array}, oczekiwano {expected}"


"""
*******************************************************
nazwa funkcji: run_tests
parametry wejściowe: brak
wartość zwracana: brak
informacje: Uruchamia testy jednostkowe
autor: 1234567890
****************************************************
"""
def run_tests():
    test_array(5, [2, 3])
    test_array(10, [2, 3, 5, 7])
    test_array(20, [2, 3, 5, 7, 11, 13, 17, 19])

    print("Testy zakończone pomyślnie")


"""
*******************************************************
nazwa funkcji: main
parametry wejściowe: brak
wartość zwracana: brak
informacje: Główna funkcja programu
autor: 1234567890
****************************************************
"""
def main():
    run_tests()
    num_count = int(input("Podaj ilość liczb: "))

    bools = []
    fill_array(bools, num_count)
    process_array(bools)

    print("Liczby pierwsze:")
    print_bool_array(bools)

main()
