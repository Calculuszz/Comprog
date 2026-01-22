LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(text):
    x = ''
    for i in text:
        if i in UPPERCASE:
            inx = UPPERCASE.index(i)
            x += UPPERCASE[(inx+13)%26]
        elif i in LOWERCASE:
            inx = LOWERCASE.index(i)
            x += LOWERCASE[(inx+13)%26]
        else:
            x += i
    return x

while True:
    s = input().strip()
    if s == 'end':
        break
    else:
        print(rot13(s))

