student1 = str(input())
student2 = str(input())

id1, gpax1, com1, calI1 ,calII1 = student1.split()
id2, gpax2, com2, calI2 ,calII2 = student2.split()

gpax1, gpax2 = float(gpax1), float(gpax2)

if com1 == 'A' and calI1 <= 'C' and calII1 <= 'C':
    status1 = True
else:
    status1 = False
if com2 == 'A' and calI2 <= 'C' and calII2 <= 'C':
    status2 = True
else:
    status2 = False

if status1 and status2:
    
    if gpax1 == gpax2:
        
        if calI1 == calI2:
            
            if calII1 == calII2:
                print("Both")
            elif calII1 > calII2:
                print(id1)
            elif calII2 > calII1:
                print(id2)
        
        elif calI1 > calI2:
            print(id1)
        elif calI2 > calI1:
            print(id2)
    
    elif gpax1 > gpax2:
        print(id1)
    elif gpax2 > gpax1:
        print(id2)

elif status1:
    print(id1)

elif status2:
    print(id2)

else:
    print("None")
    
