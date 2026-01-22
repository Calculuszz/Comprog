ids = []
grades = []

while True:
    x = input().split()
    if x[0] == 'q':
        break
    ids += [x[0]]
    grades += [x[1]]
uids = input().split()
inx = [ids.index(text) for text in uids]
p = {
    'F': 'D',
    'D': 'D+',
    'D+': 'C',
    'C': 'C+',
    'C+': 'B',
    'B': 'B+',
    'B+': 'A',
    'A': 'A'
}

for i in inx:
    grades[i] = p[grades[i]]

combined = list(zip(ids, grades))

combined_sorted = sorted(combined, key=lambda x: int(x[0])) 
#ถ้าเราใส่ key เข้าไป มันจะเป็นการบอก Python ว่า "เฮ้ย ก่อนจะเรียง ให้เอาข้อมูลแต่ละตัวไปผ่านฟังก์ชันนี้ก่อนนะ 
#แล้วค่อยเอาผลลัพธ์มาตัดสินว่าจะวางใครก่อนหลัง"
#ถ้าไม่ใส่ key เราจะเอา ids[i] ที่เป็น str มันจะเปรียบเทียบแค่ตัวแรกสุดเท่านั้น

for sid, grade in combined_sorted:
    print(sid, grade)

    

