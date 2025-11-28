#https://drive.google.com/file/d/1JGonX9kOjN0ZN4jhTAQGCoG1ho8o5mCO/view

import math

n = int(input())

a = math.sqrt(2*math.pi)
b = n**(n + 0.5)
c = math.e**(-n + 1/(12*n + 1))
low = a*b*c 

d = math.sqrt(2*math.pi)
e = n**(n + 0.5)
f = math.e**(-n + 1/(12*n))
up = d*e*f

print(low)
print(up)
