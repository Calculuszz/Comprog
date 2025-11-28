key = str(input()) #aba
main = str(input()) #abababa
c = 0
for i in range(len(main) - len(key) +1):
    if main[i:i + len(key)] == key:
        c += 1
print(c)    
