def solution(s):
    # 문자열에서 각 문자의 다음 문자를 찾아 현재 문자와 같은지 검색한다.
    # 그럼 그 짝을 삭제한 후 해당 문자열을 붙인다.
    # 다시 처음부터 작업을 수행한다.
    # 남아있는 문자열의 크기가 1또는 더 이상 검색할 수 없는 경우(ex.'abc'),
    # 0을 반환하도록 한다.
    # 남아있는 문자열의 크기가 0이면
    # 1을 반환하도록 한다.
    while len(s) >0:
        found_pair = False
        
        for index in range(len(s) - 1):
            if s[index] == s[index + 1]:
                s = s[:index] + s[index + 2:]
                found_pair = True
                break
            
        if not found_pair:
            return 0
        
    return 1

# test case

s = 'baabaa'	#result = 1
print(solution(s))

s = 'cdcd'	# result = 0
print(solution(s))

s = 'abc'	# result = 0
print(solution(s))

s = 'aaaaaabaaabcccccccbbaaa'	# result = 1
print(solution(s))