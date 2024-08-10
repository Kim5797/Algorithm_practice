def solution(X, Y):
    answer = ''
    visited_char = ''  # 방문한 문자 저장
    X_count = {} # X 문자열의 문자 개수 저장
    
    visited_char = X[0] # 방문한 문자열에 첫번째 문자 저장
    X_count[X[0]] = X.count(X[0]) # 첫번째 문자의 개수 저장
    for a in X: 
        if a not in visited_char:
            visited_char += a
            X_count[a] = X.count(a)
            
    visited_char = ''
    Y_count = {}
    visited_char = Y[0]
    Y_count[Y[0]] = Y.count(Y[0])
    for b in Y:
        if b not in visited_char:
            visited_char += b
            Y_count[b] = Y.count(b)
    
    visited_char = Y if len(X) > len(Y)  else X
    for char in visited_char:
        pass
    return answer

print(int("00"))
# print(''.join(map(str, sorted([2,3,4,51,1,6,6,2,1,1], reverse=True))))