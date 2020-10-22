# (c) TICSIA
#
#
import math

a = int(input('a > '))
b = int(input('b > '))
c = int(input('c > '))

d = (b**2) - 4 * a * c

if d >= 0:
    x1 = -d + math.sqrt(d) / (2*a)
    x2 = -d - math.sqrt(d) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
else:
    print('Корней нет')
