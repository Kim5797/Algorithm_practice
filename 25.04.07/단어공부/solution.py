S = input().upper()

char_set = set(S.upper())

char_dict = dict()

for c in char_set:
    char_dict[c] = S.count(c)

sorted_char_list = sorted(char_dict.items(), key = lambda c : c[1], reverse=True)

if len(sorted_char_list) >= 2:
    if sorted_char_list[0][1] == sorted_char_list[1][1]:
        print("?")
    else:
        print(sorted_char_list[0][0])
else:
    print(sorted_char_list[0][0])