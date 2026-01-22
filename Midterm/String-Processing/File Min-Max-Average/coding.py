s = input().strip().split()
x = [
    ['6230012121', 90.0],
    ['6130351221', 80.0],
    ['6231027921', 80.0],
    ['5830548121', 65.5],
    ['6031087221', 79.9],
    ['6230550321', 70.0],
    ['6230432721', 60.0],
    ['6230215221', 50.0],
     ]
y = []
for ids, score in x:
    if ids[:2] == s[1][2:4]:
        y.append(float(score))
if y:
    print(min(y), max(y), (sum(y) / len(y)))
else:
    print('No data')





