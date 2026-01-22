# t = 4 min
n = [int(e) for e in input().split()]
n.sort
x = []
y = 0
for i in n:
    if i not in x:
        y += 1
        x += [i]
x.sort()
print(y)
if len(x) >= 10:
    print(x[:10])
else:
    print(x)








