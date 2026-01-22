s = input() #-10-20
x = ''
if s[0] == '-' or s[0] == '+':
    x += s[0]
    for i in range(1,len(s)):
        if s[i] == '-' or s[i] == '+':
            x += ' ' + s[i]
        else:
            x+= s[i]
    print(sum([int(e) for e in x.split()]))
else:
    for i in range(len(s)):
        if s[i] == '-' or s[i] == '+':
            x += ' ' + s[i]
        else:
            x+= s[i]
    print(sum([int(e) for e in x.split()]))



        

