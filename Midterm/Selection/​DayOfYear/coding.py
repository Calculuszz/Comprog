d = str(input())
m = str(input())
y = str(input())

#law 366 วัน ใช้ค.ศ
#year % 4 == 0 and year % 100 != 0 or year % 400 == 0

common_year = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_year = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

y = y - 543

if m!=1:
    # Case 1: Leap year (Y mod 400 = 0)
    if y%400 == 0:
        print(leap_year[m-2]+d)
    # Case 2: Leap year (Y mod 4 = 0 but Y mod 100 != 0)
    elif y%4 == 0 and y%100!=0:
        print(leap_year[m-2]+d)
    # Case 3: Common year
    else:
        print(common_year[m-2]+d)
else:
    print(d)
