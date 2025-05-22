T = int(input())

for test_case in range(1, T + 1):
    선수_수 = int(input())
    A팀_선호도 = list(map(int, input().split()))
    B팀_선호도 = list(map(int, input().split()))

    선수 = [None for _ in range(선수_수)]

    A_인덱스 = 0
    B_인덱스 = 0

    for i in range(선수_수):
        if i % 2 == 0:
            while A_인덱스 < 선수_수:
                선수번호 = A팀_선호도[A_인덱스]
                A_인덱스 += 1
                if 선수[선수번호 - 1] is None:
                    선수[선수번호 - 1] = 'A'
                    break
        else:
            while B_인덱스 < 선수_수:
                선수번호 = B팀_선호도[B_인덱스]
                B_인덱스 += 1
                if 선수[선수번호 - 1] is None:
                    선수[선수번호 - 1] = 'B'
                    break

    print(''.join(선수))
