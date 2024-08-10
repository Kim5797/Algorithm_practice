def solution(num):
    answer = 0 
    number = num

    if number == 1:
        return 0
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            answer += 1
        else:
            number = number * 3 + 1
            answer += 1

        if answer == 500:
            return -1
        
    return answer

# Code test
num = 6
print(solution(num)) # Expect 8
num = 16
print(solution(num)) # Expect 4
num = 626331
print(solution(num)) # Expect -1