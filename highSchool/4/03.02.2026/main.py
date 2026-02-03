from math import sqrt, ceil

def fill_array(array, count):
    for i in range(count):
        array.append(True)

def process_array(array):
    num_count = len(array)

    for i in range(2, ceil(sqrt(num_count))):
        if array[i]:
            for j in range(2 * i, num_count, i):
                array[j] = False

def print_bool_array(array):
    for i in range(2, len(array)):
        if array[i]:
            print(i, end=" ")
    
    print()

def bool_array_to_numbers(array):
    res = []

    for i in range(2, len(array)):
        if array[i]:
            res.append(i)

    return res

def test_array(length, expected):
    array = []
    fill_array(array, length)
    process_array(array)

    assert bool_array_to_numbers(array) == expected, f"Zwrócono {array}, oczekiwano {expected}"

def run_tests():
    test_array(5, [2, 3])
    test_array(10, [2, 3, 5, 7])
    test_array(20, [2, 3, 5, 7, 11, 13, 17, 19])

    print("Testy zakończone pomyślnie")

def main():
    run_tests()
    num_count = int(input("Podaj ilość liczb: "))

    bools = []
    fill_array(bools, num_count)
    process_array(bools)

    print("Liczby pierwsze:")
    print_bool_array(bools)

main()
