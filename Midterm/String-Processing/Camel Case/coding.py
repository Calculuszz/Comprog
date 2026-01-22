s = input().strip().lower()
x = ''
for i in s:
    if i.isalnum():
        x += i
    else:
        x += ' '

x = x.split()
for j in range(1, len(x)):
    x[j] = x[j][0].upper() + x[1][1:]

print(''.join(x))
