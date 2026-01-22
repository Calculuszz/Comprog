def is_prime(n): 
    # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่ 
    if n <= 1: 
        return False 
    for k in range(2,int(n**0.5)+1): 
        if n%k == 0: 
            return False 
    return True 
# 1,3,5,7,11
def next_prime(N): # 4 --> 5
    n = N + 1
    while True:
        if is_prime(n):
            return n 
        n += 1
def next_twin_prime(N): 
    n1 = next_prime(N)
    n2 = next_prime(n1)
    while n2 - n1 != 2:
        n1 = n2
        n2 = next_prime(n2)
    return n1, n2

exec(input().strip())  