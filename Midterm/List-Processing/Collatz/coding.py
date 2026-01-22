n = int(input())
x = [str(n)]

while n != 1: 
    if n % 2 == 0: 
        n //= 2  # ปัดเศษทิ้ง 
    else: 
        n = 3 * n + 1
    x += [str(n)]
print("->".join(x[-15:-1]))