def solution(num, total):
    start = 0 - num // 2
    end = start + num

    while True:
        number = sum(range(start, end))
        if number == total:
            return list(range(start, end))
        else:
            start += 1
            end = start + num