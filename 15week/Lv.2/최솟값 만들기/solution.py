def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    C = zip(A, B)
    for i, j in C:
        answer += i*j

    return answer