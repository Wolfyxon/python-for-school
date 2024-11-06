nums_str = input("Podaj liczby do posortowania: ")
nums = []

for i in nums_str.split(" "):
    try:
        n = float(i)
        nums.append(n)

    except TypeError:
        print(f"'{f}' to nie liczba")

