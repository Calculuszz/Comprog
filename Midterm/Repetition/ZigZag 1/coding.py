x = int(input())
a = []
b = []
for i in range(x):
    x, y = [int(e) for e in input().split()]
    if i % 2 == 0:
        a += [x]
        b += [y]
    else:
        a += [y]
        b += [x]
cmd = input().strip()
if cmd == "Zig-Zag":
    print(min(a), max(b))
elif cmd == "Zag-Zig":
    print(min(b), max(a))




