s = [int(e) for e in input().split()]

def Aqi(aqi,inx):
    if aqi < 25:
        return f'{inx}..|+........'
    elif 25 <= aqi < 50:
        return f'{inx}..|..+......'
    elif 50 <= aqi < 100:
        return f'{inx}..|....+....'
    elif 100 <= aqi < 200:
        return f'{inx}..|......+..'
    elif 200 <= aqi:
        return f'{inx}..|........+'   

print('AQI|1 2 3 4 5')
print('-------------')
for i in range(len(s)):
    print(Aqi(s[i], i+1))
print('-------------')
