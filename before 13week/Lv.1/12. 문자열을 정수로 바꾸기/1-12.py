def solution(s):
    answer = 0
    array_str = list(s)
    array_str.reverse()

    for index, str in enumerate(array_str):
        if str == '+':
            return answer
        elif str == '-':
            return answer * -1
        else:
            answer += int(str) * 10**index
    return answer



# The following is code to output testcase.
s = "+12312"
# s = "-12312"
# s = "12312"
print(solution(s)) # 12312
# print(solution(s)) # -12312
# print(solution(s)) # 12312
