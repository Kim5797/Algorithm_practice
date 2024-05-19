def solution(arr):
    answer = 0
    for num in arr:
        answer += num
    answer /= len(arr)
    return answer



# The following is code to run the solution function above
arr = [1, 2, 3, 4]
print(solution(arr)) # 2.5