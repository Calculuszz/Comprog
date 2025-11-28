x1, x2, x3, x4 = [float(e) for e in input().split()]
#ลอง x1 > x2 > x3 > x4 max = x1 min = x2
if x1 > x2 and x1 > x3 and x1 > x4: #ตัด x1
    if x2 < x3 and x2 < x4:
        print(round((x3 + x4) / 2, 2)) 
    elif x3 < x4:
        print(round((x2 + x4) / 2, 2)) 
    else:
        print(round((x2 + x3) / 2, 2)) 

elif x2 > x3 and x2 > x4 : #ตัด x2
    if x1 < x3 and x1 < x4:
        print(round((x3 + x4) / 2, 2)) 
    elif x3 < x4:
        print(round((x1 + x4) / 2, 2)) 
    else:
        print(round((x1 + x3) / 2, 2)) 

elif x3 > x4: #ตัด x3
    if x1 < x2 and x1 < x4:
        print(round((x2 + x4) / 2, 2)) 
    elif x2 < x4:
        print(round((x1 + x4) / 2, 2)) 
    else:
        print(round((x1 + x2) / 2, 2)) 

else: #ตัด x4
    if x1 < x2 and x1 < x3:
        print(round((x3 + x2) / 2, 2)) 
    elif x2 < x3:
        print(round((x3 + x1) / 2, 2)) 
    else:
        print(round((x1 + x2) / 2, 2)) 
