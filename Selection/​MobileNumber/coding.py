num = str(input())

list_number = ["06", "08", "09"]

if num[0:2] in list_number and len(num) == 10:
    print("Mobile number")
else:
    print("Not a Mobile number")