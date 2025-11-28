s = str(input()) #ABBA
RLE = ''

for i in range(0, len(s)):
    if i == 0:
        character = s[0]
        c = 1
    elif s[i] == character:
        c += 1
    elif s[i] != character:
        RLE += character + " " + str(c) + " "
        character = s[i]
        c = 1

RLE += character + " " + str(c) + " "

print(RLE)