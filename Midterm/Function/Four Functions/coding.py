def make_int_list(x): 
    y = [int(e) for e in x.split()]
    return y

def is_odd(e):
    if e % 2 != 0:
        return True
    return False

def odd_list(alist):
    for i in alist:
        if is_odd(i):
            pass
        else:
            alist.remove(i)
    return alist

def sum_square(alist):
    b = []
    for i in alist:
        b.append(i ** 2)
    return sum(b)
    
exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader