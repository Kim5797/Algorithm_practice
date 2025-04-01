N, X = map(int, input().split())

A = map(int, input().split())

count = []

for num in A:
    if num < X:
        count.append(num)

print(' '.join(map(str, count)))
