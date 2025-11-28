num = int(input())

x1 = "positive"
x2 = "even"

if num < 0:
    x1 = 'negative'
if num == 0:
    x1 = 'zero'

if num % 2 != 0:
    x2 = 'odd'

print(x1)
print(x2)
