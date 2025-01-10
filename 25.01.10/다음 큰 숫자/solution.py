def solution(n):
    # n을 2진수로 변환 후 1의 개수를 센다.
    # n의 2진수 형태에서 세는 1의 개수가 n과 같으면서 값이 큰 첫번째 수가 
    # 정답이 된다.
    # 예를 들어 2(10)은 3(11)을 넘어 4(100)가 정답이 된다.
    # 5(101) -> 6(110)
    binary_of_n = bin(n)
    count_of_one = binary_of_n.count("1")
    answer = 0
    for num in range(n+1, n**2):
        if count_of_one == bin(num).count('1'):
            answer = num
            break
    return answer

# test case

n = 78
print(solution(n)) # result = 83

n = 15
print(solution(n)) # result = 23