# S = input()
   
# total = 0

# char_set = {'ABC' : 2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
# for char in S:
#     for key, value in char_set.items():
#         if char in key:
#             total += value + 1

# print(total)

S = input()

char_map = {
    **dict.fromkeys("ABC", 3),
    **dict.fromkeys("DEF", 4),
    **dict.fromkeys("GHI", 5),
    **dict.fromkeys("JKL", 6),
    **dict.fromkeys("MNO", 7),
    **dict.fromkeys("PQRS", 8),
    **dict.fromkeys("TUV", 9),
    **dict.fromkeys("WXYZ", 10),
}

total = sum(char_map[char] for char in S)

print(total)