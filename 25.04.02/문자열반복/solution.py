T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    new_s = ''
    for char in S:
        new_s = new_s + (char) * R

    print(new_s)
