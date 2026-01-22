x = [int(e) for e in input().split()] #[0, 1, 2]
y = 0
for i in range(1,len(x) -1):
    if x[i-1] < x[i] > x[i+1]:
        y += 1
print(y)
