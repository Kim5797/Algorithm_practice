N = int(input())
Sizes = map(int, input().split())
T, P = map(int, input().split())

shirts = 0

for size in Sizes:
    shirts += (size // T) + 1 if size % T != 0 else (size // T)

print(shirts)
print(f"{N // P} {N % P}")