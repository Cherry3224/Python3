for T in range(int(input())):
    N, D = map(int, input().split())

    A = input().split() #Tách thành các phần tử

    # Ghép phần sau A với phần đầu A
    print(' '.join(A[D:] + A[:D]))
