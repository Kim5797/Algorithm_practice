def solution(n):
    answer = 0
    num = list(str(n))
    num = sorted(map(int, num), reverse=True)
    answer = int(''.join(map(str, num)))
    return answer

print(solution(118372) == 873211)