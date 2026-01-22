def f1(a,b,c):
    x = []
    if a>0:
        x.append(a)
    if b>0:
        x.append(b)
    if c>0:
        x.append(c)
    return min(x)
def f2(a,b,c):
    x = []
    if a<0:
        x.append(a)
    if b<0:
        x.append(b)
    if c<0:
        x.append(c)
    return max(x)
def f3(a,b,c):
    x = a+b+c
    if x < 0:
        return str(x)[1]
    else:
        return str(x)[0]
def f4(a,b,c):
    x = a+b+c
    return str(x)[-1]
def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a,b,c)) 
    elif s1 == 0 and s2 == 1:
        print(f2(a,b,c)) 
    elif s1 == 1 and s2 == 0:
        print(f3(a,b,c)) 
    elif s1 == 1 and s2 == 1:
        print(f4(a,b,c)) 
    else:
        print('Error') 
    
exec(input().strip())