N = int(input())
number = input()

# s = list(map(int, number))

# print(sum(s))

total = sum(int(c) for c in number)

print(total)