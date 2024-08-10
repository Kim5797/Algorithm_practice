def solution(name, yearning, photo):
    answer = [0] * len(photo)
    recollection = dict(zip(name, yearning))
    score = 0
    
    for index, people in enumerate(photo):
        for person in name:
            if person in people:
                score += recollection[person]
        answer[index] = score
        score = 0
    return answer