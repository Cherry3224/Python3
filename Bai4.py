def Convert_Bin_to_Base(Binary, base): # Chuyển đổi hệ nhị phân sang hệ cơ số khác
    decimal = int(Binary, 2)

    if(base == 2):
        return Binary

    if(base == 4):
        return Base_Convert(Binary, 2)

    if(base == 8):
        return Base_Convert(Binary, 3)

    if(base == 16):
        tempVari = hex(decimal)[2:] # Cắt 0x khỏi chuỗi ( Bỏ 2 ký tự đầu tiên)

        return tempVari.upper() # Chuyển các ký tự thành chữ Hoa

def Base_Convert(Binary, base):
    while(len(Binary) % base != 0):
        Binary = '0' + Binary

    result = ''

    for i in range (0, len(Binary), base):

    # Cú pháp cắt chuỗi
        tempVari = Binary[i : i + base] # Temporary Variable

        result += str(int(tempVari, 2))

    return result

T = int(input())

for _ in range (T):

    base = int(input())

    B = input().strip()

    print(Convert_Bin_to_Base(B, base))
