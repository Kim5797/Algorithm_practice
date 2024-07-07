def solution(a, b):
    sum = 0
    if a < b:
        for num in range(a, b + 1):
            sum += num
    elif a > b:
        for num in range(b, a + 1):
            sum += num
    else:
        sum = a

    return sum