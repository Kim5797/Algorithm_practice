def solution(keymap, targets):
    answer = []
    for item in targets:
        for char in item:
            min_index = min(map(lambda key: key.index(char) if char in key else -1, keymap))
            print(min_index)
        if min_index == -1:
            answer.append(-1)
        else:
            answer.append(min_index + 1)
    return answer


