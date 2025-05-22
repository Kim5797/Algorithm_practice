T = int(input())

for test_case in range(1, T + 1):
    학생번호 = int(input())
    점수리스트 = list(map(int, input().split()))
    최빈값딕셔너리 = dict()
    최빈값 = 0

    점수셋 = set(점수리스트)

    for 점수 in 점수셋:
        최빈값딕셔너리[점수] = 점수리스트.count(점수)

    최빈값 = sorted(최빈값딕셔너리.items(), key = lambda x:x[1], reverse= True)[0][0]
    print(f'# {test_case} {최빈값}')