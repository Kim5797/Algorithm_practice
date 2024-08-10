from collections import deque

def solution(my_string):
    answer = deque()
    # my_string을 뒤집어서 answer에 넣어줍니다.
    for char in my_string:
        answer.appendleft(char)
    return ''.join(list(answer))