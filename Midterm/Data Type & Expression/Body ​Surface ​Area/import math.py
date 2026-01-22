import math

W = float(input())
H = float(input())

A = math.sqrt(W * H) / 60
B = 0.024265 * W**0.5378 * H**0.3964 
C = 0.0333 * W**(0.6157 - 0.0188*math.log(W, 10)) * H**0.3

print(A)
print(B)
print(C)