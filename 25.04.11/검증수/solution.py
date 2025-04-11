numbers = map(int, input().split())
sum_sqaured = 0

for num in numbers:
    sum_sqaured += num**2

print(sum_sqaured % 10)