def solution(X, Y):
    answer = ''
    visited = []
    for char in X:
        if char in visited:
            continue
        else:
            if char in Y:
                if Y.count(char) <= X.count(char):
                    answer += char * Y.count(char)
                elif Y.count(char) > X.count(char):
                    answer += char * X.count(char)
                visited.append(char)
        
    if answer == '':
        return "-1"
        
    if sorted(answer, reverse=True)[0] == '0':
        return "0"
    
    return ''.join(sorted(answer, reverse=True))

# The following is code to output testcase.
# X = "100"
# Y = "2345"
X = "129372316465498613413111684684513213484"
Y = "6345965198461213518434153513516846849484"
print("X:" , sorted(X, reverse=True))
print("Y:" , sorted(Y, reverse=True))
# X = "100"
# Y = "123450"
import time

start = time.time()
print(solution(X, Y)) # Expected: "00"

print("time: ", time.time() - start)