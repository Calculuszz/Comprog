a,b,c,d = [int(e) for e in input().split()]

if a > b:
    a,b = b,a
    if d >= a :
        if c > d:
            c -= a
    else :
        c += a
    b = a + c + d
elif c > a >= b:
    d += a
elif d > c:
    b += 2
else:
    b = 2*b

print(a,b,c,d)


