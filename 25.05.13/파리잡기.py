T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    checked_list = [] # size = (N - (M - 1))**2
    length = (N - (M - 1)) 
    size = length**2
    for i in range(length):
        for j in range(length):
            sub_area = [row[j:j+M] for row in area[i:i+M]]
            flat_area = [num for row in sub_area for num in row]
            checked_list.append(sum(flat_area))

    print(f'#{test_case} {max(checked_list)}')