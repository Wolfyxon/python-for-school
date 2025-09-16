def dodaj(a: float, b: float):
    return a + b

assert dodaj(2, 2) == 4
assert dodaj(1, 5) == 6
assert dodaj(4, 4) == 8
#assert dodaj(7, 3) == 5

print("Wynik:", dodaj(
    input("Podaj A: "),
    input("Podaj B: "),
))
