n = int(input())
v = []
for i in range(n):
    x, y = [float(e) for e in input().split()]
    dis = (x**2 + y**2)**0.5
    v.append([dis, i+1, x, y])
v.sort()
order, x, y = v[2][1:]
print(f"#{order}: ({x}, {y})")