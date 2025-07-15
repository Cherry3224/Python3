def find_min_number(s):
    min_number = float('inf')

    number = ''

    for c in s:
        if(c.isdigit()):
            number += c

        elif number != '':
            min_number = min(min_number, int(number))

            number = ''

    if(number != ''): # Xử lý các số ở cuối chuỗi
        min_number = min(min_number, int(number))

    return min_number

T = int(input())

for _ in range (T):
    s = input().strip() # Xoá các khoảng trắng ở đầu và cuối chuỗi

    print(find_min_number(s))

