def solution(quiz):
    answer = []
    for char in quiz:
        char_list = char.split(' ')
        if char_list[1] == '+':
            answer.append("O" if int(char_list[0]) + int(char_list[2]) == int(char_list[-1]) else "X")
        elif char_list[1] == '-':
            answer.append("O" if int(char_list[0]) - int(char_list[2]) == int(char_list[-1]) else "X")
    
    return answer