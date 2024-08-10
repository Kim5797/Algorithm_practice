def solution(n):
    answer = 0
    for num in range(n + 1):
        print(num**2, ", ", n==num**2)
        if n == num**2:
            answer = (num + 1)**2
            break
        else:
            answer = -1
    return answer

print(solution(1)) # 144