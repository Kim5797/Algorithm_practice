def solution(phone_number):
    s = '*'*(len(phone_number) - 4)
    answer = s + phone_number[-4:]
    return answer