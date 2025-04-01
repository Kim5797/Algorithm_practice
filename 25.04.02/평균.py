# N = int(input())

# scores = list(map(float, input().split()))

# max_score = max(scores)

# for index, score in enumerate(scores):
#     scores[index] = score / max_score * 100
    

# M = sum(scores) / len(scores)

# print(M)

N = int(input())

scores = list(map(float, input().split()))

max_score = max(scores)

total = sum(score / max_score * 100 for score in scores)

M = total / N

print(M)