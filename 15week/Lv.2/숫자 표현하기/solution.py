def solution(n):
    answer = 0
    total = 0
    for num in range(1, n+1):
        for number in range(num, n+1):
            total += number
            if total > n:
                total = 0
                break
            elif total == n:
                answer += 1
                total = 0
                break
    return answer