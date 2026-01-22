line = 0
min_a, max_a = 0, 0
min_b, max_b = 0, 0

while True:
    data = input().split()
    if len(data) == 1:
        cmd = data[0]
        if cmd == 'Zig-Zag':
            print(min_a, max_b)
        elif cmd == 'Zag-Zig':
            print(min_b, max_a)
        break
    x, y = int(data[0]), int(data[1])

    if line == 0:
        min_a, max_a = x, x
        min_b, max_b = y, y
    else:
        if line % 2 == 0:
            min_a, max_a = min(min_a, x), max(max_a, x)
            min_b, max_b = min(min_b, y), max(max_b, y)
        else:
            min_a, max_a = min(min_a, y), max(max_a, y)
            min_b, max_b = min(min_b, x), max(max_b, x)

    # Increment the line number
    line += 1