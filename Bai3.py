def find_max_number(n):
    max_number = 0

    number = ''

    for c in n:
        if(c.isdigit()):
            number += c

        elif(number != ''):
            max_number = max(max_number, int(number))

            number = ''

    if(number.isdigit()): # Xử lý số cuối chuỗi
        max_number = max(max_number, int(number))

    return(max_number)

T = int(input())

for _ in range(T):
    s = input().strip() # Xoá khoảng trắng

    print(find_max_number(s))
