N, M = map(int, input().split())

result = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for i in range(i - 1, j):
        result[i] = k

print(' '.join(map(str, result)))