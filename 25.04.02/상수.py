S_1, S_2 = input().split()

if int(S_1[::-1]) >= int(S_2[::-1]):
    print(S_1[::-1])
else:
    print(S_2[::-1])