h = int(input()) #8

for i in range(1,h): # 
    if i == 1: 
        print((h-1)*'.'+'*')
    else: # i = 3, h = 8 ,บรรทัด 3 ,an =  a1 +(n-1)d = 1 + (n-1)2
        print((h-i)*'.'+'*'+((1+ (i-2)*2)*'.')+'*')
print((2*h-1)*'*')