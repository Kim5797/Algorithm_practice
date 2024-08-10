def solution(absolutes, signs):
    answer = 0
    for index, number in enumerate(absolutes):
        if signs[index] == True:
            answer += number
        else:
            answer -= number
    return answer