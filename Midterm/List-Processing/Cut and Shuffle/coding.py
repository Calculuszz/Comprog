n = input().split()
y = input()

for op in y:  
    mid = len(n) // 2
    first_half = n[:mid]
    second_half = n[mid:]
    
    if op == 'C':
        # Cut: สลับครึ่งหน้ากับครึ่งหลัง
        n = second_half + first_half
    elif op == 'S':
        # Shuffle: สลับฟันปลา
        n = []
        for j in range(mid): # ใช้ j และอ้างอิง mid ที่คำนวณไว้แล้ว
            n.append(first_half[j])
            n.append(second_half[j])

print(" ".join(n))