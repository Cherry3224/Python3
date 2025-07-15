def Reducethesquence(array):

    stack = []
    for x in array:
        if stack and (stack[-1] + x) % 2 == 0:
            stack.pop()

        else:
            stack.append(x)

    return len(stack)

n = int(input())

array = list(map(int, input().split()))

print(Reducethesquence(array))


