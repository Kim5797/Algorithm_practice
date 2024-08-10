def solution(numbers):
    answer = []
    for num_index, num in enumerate(numbers):
        for index in range(len(numbers)):
            if index != num_index:
                answer.append(num + numbers[index])

    answer = sorted(set(answer))
    return answer

# The following is code to output testcase.
# numbers = [2,1,3,4,1]
# numbers = [5,0,2,7]
numbers = [0,0,0,0]
print(solution(numbers))