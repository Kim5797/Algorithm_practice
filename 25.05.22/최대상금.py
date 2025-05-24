
def solve_max_number(num_str, 교환횟수):
    """
    DFS + 메모이제이션을 사용하여 최대값을 구하는 함수
    """
    num = list(num_str)
    n = len(num)
    memo = {}
    
    def dfs(current_num, 남은횟수):
        # 현재 상태를 키로 사용
        state = (''.join(current_num), 남은횟수)
        
        if state in memo:
            return memo[state]
        
        # 교환 횟수가 0이면 현재 숫자 반환
        if 남은횟수 == 0:
            result = ''.join(current_num)
            memo[state] = result
            return result
        
        max_result = ''.join(current_num)
        
        # 모든 가능한 교환 시도
        for i in range(n):
            for j in range(i + 1, n):
                # i번째와 j번째 위치 교환
                current_num[i], current_num[j] = current_num[j], current_num[i]
                
                # 재귀 호출
                result = dfs(current_num, 남은횟수 - 1)
                
                # 더 큰 숫자인지 비교
                if int(result) > int(max_result):
                    max_result = result
                
                # 원상복구(백트래킹)
                current_num[i], current_num[j] = current_num[j], current_num[i]
        
        memo[state] = max_result
        return max_result
    
    return dfs(num, 교환횟수)


T = int(input())
for test_case in range(1, T + 1):
    num, 교환횟수 = input().split()
    교환횟수 = int(교환횟수)
    
    # 최대값 계산
    result = solve_max_number(num, 교환횟수)
    
    print(f'#{test_case} {result}')