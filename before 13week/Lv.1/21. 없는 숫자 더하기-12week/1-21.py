def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for number in num:
        if number not in numbers:
            answer += number
    return answer

# The following is code to output testcase.
numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers)) # Expected: 14
