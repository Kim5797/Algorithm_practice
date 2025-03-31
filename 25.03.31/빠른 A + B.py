import sys

T = int(sys.stdin.readline().strip())
results = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    results.append(a + b)

sys.stdout.write('\n'.join(map(str, results)) + '\n')


