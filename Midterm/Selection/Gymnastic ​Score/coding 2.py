a, b, c, d = [float(e) for e in input().split()]

sum = a + b + c + d

min = a
if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d

max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d

sum -= min + max

avg = round(sum/2,2)
print(avg)
