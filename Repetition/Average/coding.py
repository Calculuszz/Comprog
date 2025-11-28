s = 0
n = 0
x = input()
if x == 'q':
    print('No Data')
else:
    while x != 'q':
        s += float(x)
        n += 1
        x = input()
    print(round(s / n, 2))