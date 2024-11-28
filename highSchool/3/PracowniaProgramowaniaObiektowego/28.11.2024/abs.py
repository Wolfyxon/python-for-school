from util import inputf

n = inputf("Podaj liczbę: ")

if n < 0: 
    n = -n

print("Wartość bezwzględna:", n)