def solution(n):
    answer = []
    array = list(str(n))
    array.reverse()
    for num in array:
        answer.append(num)
    return answer