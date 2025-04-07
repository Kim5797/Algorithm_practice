l = [-1] * 26

S = input()
main_index = 0


for index, char in enumerate(S):
    if l[ord(char) - ord('a')] == -1:
        l[ord(char) - ord('a')] = index

# print(" ".join(map(str, l)))
print(*l)