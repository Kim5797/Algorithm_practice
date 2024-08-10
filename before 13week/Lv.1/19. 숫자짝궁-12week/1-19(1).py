def solution(X, Y):
    answer = []
    visited_char = dict()  # 방문한 문자 저장
    is_Zero = []
    visited_char[X[0]] = X.count(X[0])  # 첫번째 문자의 개수 저장

    for a in X:
        visited_char[a] = X.count(a)

    for char, count in visited_char.items():
        if char in Y:
            if char == '0':
                is_Zero.append(True)
            else:
                is_Zero.append(False)
                
            if count > Y.count(char):
                answer.append(char * Y.count(char))
            else:
                answer.append(char * count)
    if answer == []:
        return '-1'
    print(answer)
    if any(answer) == False:
        return '0'
    
    return ''.join(sorted(answer, reverse=True))

# The following is code to output testcase.
# X = "100"
# Y = "2345"
# X = "100"
# Y = "203045"
X = "100"
Y = "123450"

print(solution(X, Y)) # Expected: "00"