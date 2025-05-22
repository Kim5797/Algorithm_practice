T = int(input())
for index in range(1, T + 1):
    N = int(input())
    매매가들 = list(map(int, input().split(' ')))
    이익 = 0
    최대매매가 = 0
    
    if 매매가들[0] == max(매매가들):
        print(f'#{index} 0')
        continue
    
    for 매매가 in reversed(매매가들):
        if 최대매매가 < 매매가:
            최대매매가 = 매매가
        else:
            이익 += 최대매매가 - 매매가
    print(f'#{index} {이익}')
    index += 1
    
    
