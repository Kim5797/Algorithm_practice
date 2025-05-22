# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    N, hexa = input().split()
    N = int(N)
    S = ''

    for c in hexa:
        S += bin(int(c, base=16))[2:].zfill(4)

    print(f'#{test_case} {S}')