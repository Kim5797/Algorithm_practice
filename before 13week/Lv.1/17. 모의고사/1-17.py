def solution(answers):
    patterns =[
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]

    for index, correct_answer in enumerate(answers):
        for pattern_index, pattern in enumerate(patterns):
            if correct_answer == pattern[index % len(pattern)]:
                scores[pattern_index] += 1


    max_score = max(scores)

    answer = [index + 1 for index, score in enumerate(scores) if score == max_score]
    return answer

