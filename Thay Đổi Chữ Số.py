def Convert(q, p, s : str): # s : str (Ép kiểu string cho s)
    return int(s.replace(str(q), str(p)))

for _ in range(int(input())):
    q, p = input().split()

    while True: # Xử lý input ko sạch
        line = input().strip()

        if line:
            break

    if len(line.split()) == 2:
        X1, X2 = line.split()

    else:
        X1 = line

        X2 = input().strip()

    print(Convert(p, q, X1) + Convert(p, q, X2), Convert(q, p, X1) + Convert(q, p, X2))
