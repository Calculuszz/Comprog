a,b,c,d = [int(e) for e in input().split()]
if d>a:
    n = 0
    while a<d:
        n+= 1
        a+= abs(b)
        d+= -abs(c)
    print(n,a,d)
else:
    a,d = d,a
    if a>b:
        a,b = b,a
    if c>d:
        c,d=d,c
    if b==c:
        print(a,b,d)
    else:
        if b>c:
            print((b+c)/2)
        else:
            print(a,b,c,d)