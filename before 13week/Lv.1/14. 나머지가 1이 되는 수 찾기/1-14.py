def solution(n):
    answer = 0
    for num in range(2, n):
        if (n - 1) % num == 0:
            answer = num
            break
    return answer