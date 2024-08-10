def solution(n):
    answer = 1
    already_in = [1]
    for num in range(2, n + 1):
        if n % num == 0 and n not in already_in:
            answer += 1
            already_in.append(num)
    return answer