from typing import Callable
from time import time, sleep

nums_str = input("Podaj liczby do posortowania: ")
nums = []

for i in nums_str.split(" "):
    try:
        n = float(i)
        nums.append(n)

    except TypeError:
        print(f"'{f}' to nie liczba")
        exit(1)

ln = len(nums)

if ln <= 1:
    print("Ilość liczb musi być większa niż 1, inaczej sortowanie nie ma sensu")
    exit(1)

print()

def sort(name: str, callback: Callable):
    start = time()

    cloned = nums.copy()
    callback(cloned)

    duration = time() - start
    print(f"Sortowanie {name} zajęło: {duration} sekund.")
    print(cloned)

def selection(nums):
    for i in range(ln):
        min_v = min(nums[i:ln])
        min_idx = nums.index(min_v)

        nums[min_idx] = nums[i]
        nums[i] = min_v

def bubble(nums):
    while True:
        sorted = True

        for i in range(ln):
            sorted = True

            prev_idx = i - 1

            if prev_idx < 0:
                sorted = False
                continue

            if nums[i] < nums[prev_idx]:
                prev = nums[prev_idx]
                current = nums[i]

                nums[i] = prev
                nums[prev_idx] = current

                sorted = False

        if sorted:
            break    


def insertion(nums):
    while True:
        sorted = True

        for i in range(ln):
            sorted = True

            prev_idx = i - 1

            if prev_idx < 0:
                sorted = False
                continue

            if nums[i] < nums[prev_idx]:
                prev = nums[prev_idx]
                current = nums[i]

                nums[i] = prev
                nums[prev_idx] = current

                sorted = False
                break

        if sorted:
            break    

sort("wybierające", selection)
sort("bąbelkowe", bubble)
sort("wstawiające", insertion)