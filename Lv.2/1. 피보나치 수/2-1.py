def solution(n):
    fibo = list()
    fibo.append(0)
    fibo.append(1)
    for i in range(1, n, 1):
        fibo.append(fibo[i] + fibo[i-1])
    answer = fibo[n] % 1234567
    return answer

# The following is code to execute the solution function and print its result.
print(solution(3)) # 2
print(solution(5)) # 5
print(solution(100)) # 687995182