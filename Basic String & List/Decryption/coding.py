num = str(input())

a = int(num[3] + num[10] + num[17] + num[24] + num[31])
b = int(num[7] + num[12] + num[17] + num[22] + num[27])

x = str(a + b + 10000)[-4:-1]
z = int(x[0]) + int(x[1]) + int(x[2])
q = z % 10 + 1
abc__ = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
ans = str(x)+abc__[q]

print(ans)

