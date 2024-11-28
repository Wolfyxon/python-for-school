import math
from util import inputf


print("f(x) = ax^2 + bx + c")

a = inputf("Podaj A: ")
b = inputf("Podaj B: ")
c = inputf("Podaj C: ")

dt = b**2 - 4 * a * c

print("Delta:", dt)

if dt == 0:
    print('x0', -b / (2 * a))

elif dt > 0:
    sqrtDt = math.sqrt(dt)

    print("x1", (-b - sqrtDt) / (2 * a))
    print("x2", (-b + sqrtDt) / (2 * a))
    
elif dt < 0:
    print("co")