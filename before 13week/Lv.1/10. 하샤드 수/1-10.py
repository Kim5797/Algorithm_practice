import numpy as np

def solution(x):
    answer = True
    num_list = list()

    for num in (str(x)):
        num_list.append(int(num))

    sum = np.sum(num_list)

    answer = bool(x % sum == 0)
    return answer
