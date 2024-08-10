def solution(keymap, targets):
    answer = [0] * len(targets)
    
    for target_index, pattern in enumerate(targets):
        for char in pattern:
            for index, key in enumerate(keymap):
                print(char, key)
                if char == key:
                    answer[target_index] += index + 1
                    break
        
        if answer[target_index] == 0:
            answer[target_index] = -1
                    
    return answer