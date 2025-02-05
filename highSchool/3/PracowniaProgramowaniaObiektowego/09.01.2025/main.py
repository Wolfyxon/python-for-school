#"I", "V", "X", "L", "C", "D", "M"
roman_nums = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}

keys = sorted(list(roman_nums.keys()), reverse=True)

arab = int(input("Podaj liczbę arabską: "))
roman = ""

if arab <= 0:
    print("Liczba musi być wieksza od 0")
    exit(1)


while arab > 0:
    for key in keys:
        while arab >= key:
            roman += roman_nums[key]
            arab -= key

print(roman)