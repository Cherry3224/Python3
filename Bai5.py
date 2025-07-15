def to(a, b, s: str): # s : str (Ép kiểu string cho s)
    return int(s.replace(str(a), str(b)))

for _ in range(int(input())):
    a, b = input().split()

    while True:
        line = input().strip()

        if line:
            break
    if len(line.split()) == 2:
        x1, x2 = line.split()

    else:
        x1 = line

        x2 = input().strip()

    print(to(b, a, x1) + to(b, a, x2), to(a, b, x1) + to(a, b, x2))

