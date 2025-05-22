# for test_case in range(1, 11):  # 테스트 케이스는 1부터 10까지
#     N = int(input())
#     buildings = list(map(int, input().split()))
    
#     view_count = 0  # 조망권이 확보된 세대 수
    
#     # 양쪽 2칸씩은 항상 0이므로 그 사이의 건물들만 검사
#     for i in range(2, N-2):
#         # 현재 건물의 높이
#         current_height = buildings[i]
        
#         # 좌우 2칸 내의 가장 높은 건물 찾기
#         max_height_around = max(
#             buildings[i-2], buildings[i-1],
#             buildings[i+1], buildings[i+2]
#         )
        
#         # 현재 건물이 주변 건물보다 높다면 조망권 확보
#         if current_height > max_height_around:
#             # 조망권이 확보된 세대 수 = 현재 건물 높이 - 주변 가장 높은 건물 높이
#             view_count += current_height - max_height_around
    
#     print(f'#{test_case} {view_count}')

from collections import deque

for index_test_case in range(1):
    N = int(input())
    건물들 = list(map(int, input().split()))
    
    대상건물들 = deque(maxlen = 5)
    for index in range(5):
        대상건물들.append(건물들[index])
    전망권 = 0

    건물 = 대상건물들[2] 
    가장높은이전건물 = max(대상건물들[0], 대상건물들[1])
    가장높은다음건물 = max(대상건물들[3], 대상건물들[4])
    
    if 건물 > 가장높은이전건물 and 건물 > 가장높은다음건물:
        전망권 += min(건물 - 가장높은이전건물, 건물 - 가장높은다음건물)
    
    for 다다다음건물 in 건물들[5:]:
        대상건물들.append(다다다음건물)  # maxlen으로 인해 자동으로 맨 왼쪽 건물 제거
        
        건물 = 대상건물들[2]  # 가운데 건물
        가장높은이전건물 = max(대상건물들[0], 대상건물들[1])
        가장높은다음건물 = max(대상건물들[3], 대상건물들[4])
        # 양쪽 모두 현재 건물보다 낮아야 조망권 확보
        if 건물 > 가장높은이전건물 and 건물 > 가장높은다음건물:
            전망권 += min(건물 - 가장높은이전건물, 건물 - 가장높은다음건물)
        

            
    print(f'#{index_test_case} {전망권}')