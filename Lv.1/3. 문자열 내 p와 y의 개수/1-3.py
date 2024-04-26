def solution(s):
    answer = True
    count = 0
    
    for char in s:
        char = char.lower()
        if char == 'p':
            count += 1
        elif char == 'y':
            count -= 1

    if count == 0:
        answer = True
    else:
        answer = False
    
    return answer

# Status: Accepted
print(solution("pPoooyY")) # True
print(solution("Pyy")) # False