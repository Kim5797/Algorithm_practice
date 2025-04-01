N = input()
del N


# l = list(map(int, input().split()))
# print(f'{min(l)} {max(l)}')
l = map(int, input().split())
min_val, max_val = float('inf'), float('inf')

for num in 1:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(f'{min_val}, {max_val}')