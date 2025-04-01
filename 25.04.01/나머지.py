# all_rest = []

# for _ in range(10):
#     num = int(input())
#     rest = num % 42
#     if rest not in all_rest:
#         all_rest.append(num % 42)

# print(len(all_rest))

all_rest = set()

for _ in range(10):
    num = int(input())
    rest = num % 42
    all_rest.add(rest)

print(len(all_rest))