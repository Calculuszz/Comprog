import math as m

a = float(input())
b = float(input())
c = float(input())

x1 = (-b - (m.sqrt(b**2 - 4*a*c))) / (2*a)
x2 = (-b + (m.sqrt(b**2 - 4*a*c))) / (2*a)

print(round(x1, 3), round(x2, 3))
