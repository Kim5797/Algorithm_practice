def solution(a, b):
    if int(str(a) + str(b)) < int(str(b) + str(a)):
        return int(str(b) + str(a))
    else:
        return int(str(a) + str(b))
    

def solution(a, b):
    return int(max(f'{a}{b}', f'{b}{a}'))