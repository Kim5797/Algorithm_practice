def solution(t, p):
    answer = 0
    sliced = ''
    for index in range(len(t) - len(p) + 1):
        sliced = t[index:(index + len(p))]
        if int(sliced) <= int(p):
            answer += 1
    return answer