def solution(my_string):
    answer = 0
    for item in my_string:
        if item.isdecimal():
            answer += int(item)
    return answer