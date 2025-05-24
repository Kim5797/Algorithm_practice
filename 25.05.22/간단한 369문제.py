N = int(input())

result = []
for i in range(1, N + 1):
    num_str = str(i)
    temp = []
    for num in num_str:
        if num == '3' or num == '6' or num == '9':
            if '-' in temp:
                temp.append('-')
            else:
                temp = ['-']
        else:
            if '-' not in temp:
                temp.append(num)
    result.append(''.join(temp))
print(' '.join(result))

print(
    ' '.join(result) == '1 2 - 4 5 - 7 8 - 10 11 12 - 14 15 - 17 18 - 20 21 22 - 24 25 - 27 28 - - - - -- - - -- - - -- 40 41 42 - 44 45 - 47 48 - 50 51 52 - 54 55 - 57 58 - - - - -- - - -- - - -- 70 71 72 - 74 75 - 77 78 - 80 81 82 - 84 85 - 87 88 - - - - -- - - -- - - -- 100'

)