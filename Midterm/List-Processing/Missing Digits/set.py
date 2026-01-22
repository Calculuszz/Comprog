x = input()
y = set("0123456789")
z = {i for i in x if i.isdecimal()}
v = y - z

if not v:
    print("None")
else:
    v = sorted(list(v))
    print(",".join(v))