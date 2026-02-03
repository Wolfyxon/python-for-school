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

def print_array(array):
    for i in range(2, len(array)):
        if array[i]:
            print(i, end=" ")
    
    print()

def main():
    num_count = int(input("Podaj ilość liczb: "))

    numbers = []
    fill_array(numbers, num_count)
    process_array(numbers)

    print("Liczby pierwsze:")
    print_array(numbers)

main()
