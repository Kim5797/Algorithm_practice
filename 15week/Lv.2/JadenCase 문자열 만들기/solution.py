def solution(s):
    answer = []
    my = s.split(' ')
    for char in my:
        char = char.capitalize()
        answer.append(char)
    
    return ' '.join(answer)

print(solution("3people unFollowed me"))


