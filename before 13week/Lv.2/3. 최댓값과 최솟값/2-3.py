def solution(s):
    answer = '' 
    array = s.split(' ')
    array = list(map(int, s.split(' ')))
    answer = "{0} {1}".format(min(array), max(array))
    return answer

# The following is code to output testcase.
s = "-1 -2 -3 -4"

print(solution(s)) # "-4 -1"