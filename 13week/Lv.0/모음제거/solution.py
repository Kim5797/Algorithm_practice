def solution(my_string):
    answer = ''
    for gather in ['a', 'e', 'i', 'o', 'u']:
        if gather in my_string:
            answer = my_string.replace(gather, ' ')
    return answer