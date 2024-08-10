def solution(num_list):
    from collections import deque
    answer = deque()
    for num in num_list:
        answer.appendleft(num)
    return list(answer)