N = int(input())
l = map(int, input().split())
v = int(input())

# print(l.count(v))
count = 0
for num in l:
    if num == v:
        count += 1

print(count)
