for T in range(int(input())):
    N, D = map(int, input().split())

    A = input().split() #Nhập có dấu cách

    # Ghép phần sau D với phần đầu D
    print(' '.join(A[D:] + A[:D]))
