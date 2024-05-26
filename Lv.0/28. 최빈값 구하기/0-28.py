def solution(array):
    answer = 0
    count_dict = {}
    for num in array:
        if num not in count_dict:
            count_dict[num] = array.count(num)

    for key, value in count_dict.items():
        if value == max(count_dict.values()):
            if answer != 0:
                return -1
            answer = key
    
    return answer
