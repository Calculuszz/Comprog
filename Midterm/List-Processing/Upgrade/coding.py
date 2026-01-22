ids = []
grades = []
uids = []
#รับข้อมูล
while True:
    x = input().split()
    if x[0] == "q":
        break
    ids.append(x[0])
    grades.append(x[1])
uids.extend(input().split())
#logic
idx = [ids.index(text) for text in uids]
upgrade = {
    'F': 'D',
    'D': 'D+',
    'D+': 'C',
    'C': 'C+',
    'C+': 'B',
    'B': 'B+',
    'B+': 'A',
    'A': 'A'
}
for i in idx:
    grades[i] = upgrade[grades[i]]

for i in range(len(ids)):
    print(ids[i], grades[i])



    
