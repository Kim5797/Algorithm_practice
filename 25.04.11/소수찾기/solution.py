from math import sqrt

N = int(input())
numbers = list(map(int, input().split()))

if 1 in numbers:
    numbers.remove(1)

result_count = 0

for num in numbers:
    is_prime = True

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        result_count += 1

print(result_count)