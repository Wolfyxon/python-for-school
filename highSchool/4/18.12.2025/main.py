import math
from typing import Self

class Ulamek:
    def __init__(self, licznik: int, mianownik: int = 1) -> None:
        self.licznik = licznik
        self.mianownik = mianownik

        assert is_int_like(licznik), "Licznik musi być liczbą całkowitą"
        assert is_int_like(mianownik), "Mianownik musi być liczbą całkowitą"
        assert mianownik != 0, "Mianownik nie może być 0"

    def __str__(self) -> str:
        return f"{self.licznik}/{self.mianownik}"

    def __add__(self, value) -> Self:
        if is_int_like(value):
            value = Ulamek(value)

        if isinstance(value, Ulamek):
            u1, u2 = self.uwspolnij(value)

            return Ulamek(
                u1.licznik + u2.licznik,
                u1.mianownik
            )

        raise "Nieobsługiwana wartość dodawania"

    def __sub__(self, value) -> Self:
        if is_int_like(value):
            value = Ulamek(value)

        if isinstance(value, Ulamek):
            u1, u2 = self.uwspolnij(value)

            return Ulamek(
                u1.licznik - u2.licznik,
                u1.mianownik
            )

        raise "Nieobsługiwana wartość dodawania"

    def __mul__(self, value) -> Self:
        if isinstance(value, int):
            return Ulamek(
                self.licznik * value,
                self.mianownik * value
            )
        if isinstance(value, Ulamek):
            return Ulamek(
                self.licznik * value.licznik,
                self.mianownik * value.mianownik
            )

        raise "Nieobsługiwana wartość dla mnożenia"

    def __truediv__(self, value) -> Self:
        if is_int_like(value):
            value = Ulamek(value)

        return self * value.odwroc()

    def __div__(self, value) -> Self:
        return self.__truediv__(value)

    def uwspolnij(self, value) -> tuple[Self, Self]:
        u1 = self.skroc()
        u2 = value.skroc()

        if u1.mianownik != u2.mianownik:
            mul = u1.mianownik * u2.mianownik
            
            u1.mianownik = mul
            u2.mianownik = mul

        return (u1, u2)

    def odwroc(self) -> Self:
        return Ulamek(self.mianownik, self.licznik)

    def wartosc(self) -> float:
        return self.licznik / self.mianownik

    def skroc(self) -> Self:
        nwd = math.gcd(self.licznik, self.mianownik)

        if not is_int_like(nwd):
            return self
        
        return Ulamek(
            int(self.licznik / nwd),
            int(self.mianownik / nwd)
        )
    
def is_int_like(n: float | int) -> bool:
    return (
        isinstance(n, int)
        or 
        (isinstance(n, float) and math.floor(n) == n)
    )

ul1 = Ulamek(3, 6).skroc()
print(ul1)

ul2 = Ulamek(1, 2) * Ulamek(1, 2)
print(ul2)

u3 = Ulamek(5, 10) + Ulamek(1, 2)
print(u3)

u4 = Ulamek(1, 2) / 4
print(u4)

try:
    u5 = Ulamek(1, 0)
except AssertionError as e:
    print(e)

try:
    u5 = Ulamek(1.5, 0)
except AssertionError as e:
    print(e)

try:
    u5 = Ulamek("7", 0)
except AssertionError as e:
    print(e)
