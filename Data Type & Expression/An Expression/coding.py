import math as m

a = m.pi
b = m.factorial(10) / 8**8
c = m.log(9.7)**((7/m.sqrt(71))-m.sin(m.radians(40)))
d = 1.2**(2.3**(1/3))

print(round((a-b+c)/d, 6))