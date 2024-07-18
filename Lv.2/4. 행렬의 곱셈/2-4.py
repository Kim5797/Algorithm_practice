def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j] * arr2[j][k]
            
    return answer

# The following is code to output testcase.
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2)) # Expected output: [[15, 15], [15, 15], [15, 15]]
# print(solution(arr1, arr2)) # Expected output: [[22, 22, 11], [36, 28, 18], [29, 20, 14]]