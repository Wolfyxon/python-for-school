def inputf(query: str) -> float:
    try:
        return int(input(query))
    except ValueError:
        print("Niepoprawna liczba")
        return inputf(query)
    
a = inputf("Podaj A: ")
b = inputf("Podaj B: ")

print(a + b)