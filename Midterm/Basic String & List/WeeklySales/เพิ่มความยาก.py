sales = str(input())
sales = list(map(int,sales.split()))

total = sum(sales)
avg = total / 7

max_value = max(sales)
max_days = [i+1 for i,val in enumerate(sales) if val == max_value]

min_value = min(sales)
min_days = [i + 1 for i,val in enumerate(sales) if val == min_value]

above_avg_count = sum([1 for i in sales if i > avg])

print('ยอดรวม:',total)
print('ค่าเฉลี่ย:',round(avg,2))
print('วันขายสูงสุด:', " ".join([f"วันที่ {day}" for day in max_days]))
print('วันขายต่ำสุด:'," ".join(f"วันที่ {day}" for day in min_days))
print('จำนวนวันที่ขายมากกว่าค่าเฉลี่ย:',above_avg_count)