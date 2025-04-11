T = int(input())

for _ in range(T):
    AA = 0
    BB = 0
    H, W, N = map(int, input().split())
    if N % H == 0:
        AA = H
        BB = N // H
        print(f"{AA}{BB:02}")
    else:
        AA = N % H
        BB = N // H + 1
        print(f"{AA}{BB:02}")
