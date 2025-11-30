u = str(input())
v = str(input())

u1, u2, u3 = list(map(float, u.strip("[] ").split(", ")))
v1, v2, v3 = list(map(float, v.strip("[] ").split(", ")))
ans = [u1+v1, u2+v2, u3+v3]

print(u,'+',v,'=', ans)