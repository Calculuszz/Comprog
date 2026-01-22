s1 = input().strip().lower()
s2 = input().strip().lower()
d = 'abcdefghijklmnopqrstuvwsyz0123456789'
x1 = [0]*len(d) 
x2 = [0]*len(d) 

for char in s1:
    if char in d:
        inx = d.index(char)
        x1[inx] += 1 

for char in s2:
    if char in d:
        inx = d.index(char)
        x2[inx] += 1 

if x1 == x2:
    print('Yes')
else:
    print('No')


