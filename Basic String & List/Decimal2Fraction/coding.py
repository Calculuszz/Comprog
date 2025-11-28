import math as m

num = str(input())
a, b, c = num.split(",")
#Example: 10.23456456456... (A=10, B=23, C=456)
# Given X = 10.23456456456...
#          X = 10.23456456456...
#   (10**2)X = 1,023.456456456...
#   (10**5)X = 1,023,456.456456...
#          X = (1,023,456 - 1,023)/(10^5 - 10^2)
numerator = int(a + b + c) - int(a + b)
denominator = 10**(len(b) + len(c)) - 10**len(b)

gcd = m.gcd(numerator, denominator)
print(numerator//gcd,"/",denominator//gcd)