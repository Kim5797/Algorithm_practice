def solution(n):
    answer = 0
    if n % 2 == 0:
        for num in range(1, n+1):
            if num % 2 == 0:
                answer += num**2
    else:
        for num in range(1, n+1):
            if num % 2 != 0:
                answer += num
    return answer