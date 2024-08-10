def solution(n, k):
    answer = 0
    if n > 9:
        answer = max(0, k - n // 10 ) * 2000
    else: 
        answer = k * 2000
    answer += n * 12000
    return answer
