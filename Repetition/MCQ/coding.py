ans = str(input())
stu = str(input())
s = 0
if len(ans) == len(stu):
    for i in range(0,len(ans)):
        if ans[i] == stu[i]:
            s += 1
        else:
            pass
    print(s)
else:
    print('Incomplete answer')