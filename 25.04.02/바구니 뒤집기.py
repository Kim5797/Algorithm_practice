# N, M = map(int, input().split())

# bucket = list(range(1, N + 1))

# for _ in range(M):
#     i, j = map(int, input().split())
#     while i < j:
#         bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i - 1]
#         i += 1
#         j -= 1


# print(' '.join(map(str, bucket)))

N, M = map(int, input().split())

bucket = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    sub_list = bucket[i - 1:j]
    sub_list.reverse()
    bucket[i - 1:j] = sub_list


print(' '.join(map(str, bucket)))