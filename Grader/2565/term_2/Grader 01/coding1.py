def rotate_left(s, n): 
    return s[n:]+s[0:n]
def rotate_right(s, n): 
    return s[-n:] + s[0:-n]
def str_mod(s, n):
    x = ''
    for i in range(len(s)):
        x += str(int(s[i]) % n)
    return x
def main(): 
    s = input()
    l = int(s[-2])
    if l == 1:
        print(rotate_left(s, int(s[-1]))) 
    elif l == 2:
        print(rotate_right(s, int(s[-1]))) 
    elif l == 3:
        print(str_mod(s, int(s[-1]))) 
    else:
        print(s) 
exec(input().strip()) #ต้องมีบรรทัดนีÊเมืÉอส่งไป grader 
 