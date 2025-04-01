# l = list(range(1, 31))

# for _ in range(28):
#     l.remove(int(input()))

# print(f"{min(l)}\n{max(l)}")

l = set(range(1, 31))

for _ in range(28):
    l.remove(int(input()))

m = sorted(l)
print(f"{m[0]}\n{m[1]}")