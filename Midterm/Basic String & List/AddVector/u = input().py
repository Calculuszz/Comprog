u = [float(e) for e in input().strip('[] ').split(', ')]
v = [float(e) for e in input().strip('[] ').split(', ')]
ans = [a + b for a, b in zip(u, v)]

print(u, '+', v, '=', ans)
