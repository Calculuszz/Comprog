x = int(input())
ans = []
for i in range(x):
    ans.append(int(input()))

ans += [int(e) for e in input().split()]

while True:
    v = int(input())
    if v == -1:
        break
    ans.append(v)
p = []
for i in range(len(ans)):
    if i % 2 == 0:
        p.append(ans[i])
    else:
        p.insert(0, ans[i])
print(p)


