num = str(input())

x1 = int(num[3]+num[10]+num[17]+num[24]+num[31])
x2 = int(num[7]+num[12]+num[17]+num[22]+num[27])

sum_x = str(x1 + x2 + 10000)

mod_sum_x = sum_x[-4:-1] #เราต้องนับจากข้างหลังมาข้างหน้าเพราะนับตามหลักพัน ร้อย สิบ

y = int(mod_sum_x[0]) + int(mod_sum_x[1]) +int(mod_sum_x[2])
mod_y = y%10 + 1 #ลองกลับมาคิด

dic = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H",
    9:"I",
    10:"J"
}
print(str(mod_sum_x)+dic[mod_y])