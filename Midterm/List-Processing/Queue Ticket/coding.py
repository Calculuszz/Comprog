q = [] 
m = int(input()) 
customer = 0
n = 0
queue_time = []

for k in range(m): 
    c = input().split() 
    if c[0] == 'reset':
        n = int(c[1])
    elif c[0] == 'new': 
        print(f'ticket {n}')
        # แก้จาก { } เป็น [ ] และใส่ int() ครอบเวลาซะ
        q.append([n, int(c[1])]) 
        n += 1 
    elif c[0] == 'next': 
        # เรียก index [0] ได้แล้วเพราะ q เก็บเป็น list ย่อย
        print(f'call {q[customer][0]}')
        customer += 1
    elif c[0] == 'order': 
        current_ticket, new_time = q[customer - 1]
        order_time = int(c[1])
        delta = order_time - new_time # แก้คำสะกด delta
        print(f'qtime {current_ticket} {delta}') 
        queue_time.append(delta)
    elif c[0] == 'avg_qtime': 
        # กันเหนียวเรื่องหารด้วยศูนย์
        if len(queue_time) == 0:
            print("avg_qtime 0.0")
        else:
            avg = sum(queue_time) / len(queue_time)
            print("avg_qtime", round(avg, 4))
# reset n 
# เก็บ x = n
# new t --> n , n += 1 (เลขคิวจากเพิ่มขึ้น 1 ต่อเมื่อ new t)
# q.append([n, t])
#นิยาม pointer = 0 
# next -- call q[pointer][0] ,pointer += 1
# order --> delta = order_time - q[pointer -1][1]
#