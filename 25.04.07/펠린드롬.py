S = input()
result = 1

for num in range(len(S) // 2):
    if S[num] != S[len(S) - 1 - num]:
        result = 0
        break

print(result)