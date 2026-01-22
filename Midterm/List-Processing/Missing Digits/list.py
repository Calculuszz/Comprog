# t = 4.39 min
x = input()
y = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in x:
    if i in y:
        y.remove(i)
if y :
    print(','.join(y))
else:
    print("None")

