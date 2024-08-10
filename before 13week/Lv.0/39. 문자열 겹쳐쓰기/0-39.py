def solution(my_string, overwrite_string, s):
    pre = my_string[:s]
    post = my_string[s + len(overwrite_string):]
    answer = pre + overwrite_string + post
    return answer