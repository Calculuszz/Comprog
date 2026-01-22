#t = 3.00 min
REAL_NAMES = [
    "Robert",
    "William",
    "James",
    "John",
    "Margaret",
    "Edward",
    "Sarah",
    "Andrew",
    "Anthony",
    "Deborah",
]
NICKNAMES = [
    "Bob",
    "Bill",
    "Jim",
    "Jack",
    "Peggy",
    "Ed",
    "Sally",
    "Andy",
    "Tony",
    "Debbie",
]

# Input amount of names
n = int(input())

# Output the corresponding nicknames
for _ in range(n):
    name = input().strip()
    # Output the nickname if found
    if name in REAL_NAMES:
        idx = REAL_NAMES.index(name)
        print(NICKNAMES[idx])
    # Output the real name if found
    elif name in NICKNAMES:
        idx = NICKNAMES.index(name)
        print(REAL_NAMES[idx])
    # Output "Not found" if neither is found
    else:
        print("Not found")