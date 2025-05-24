T = int(input())

for test_case in range(1, T + 1):
    S = input()
    base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    decoded_S = ''
    for i in range(len(S) // 4):
        temp = [S[i*4], S[i*4+1], S[i*4+2], S[i*4+3]]
        print(temp)
        buffer_S = ''
        for char in temp:
            buffer_S += bin(base64_table.index(char))[2:].rjust(6, '0')

        print(buffer_S)
        for start in range(3):
            temp_S = buffer_S[start*8:start*8+8]
            decoded_S += chr(int(temp_S, base=2))

    print(f'#{test_case} {decoded_S}')