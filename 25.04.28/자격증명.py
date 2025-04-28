# https://pyalgo.co.kr/?page=1

def solution(data):
    result = ''
    for 암호문 in data:
        암호문 = 암호문.replace('+', '1').replace('-', '0').replace(' ', '')
        result += chr(int(암호문, base=2))
    return result

print(solution([' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - ']))