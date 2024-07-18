## 문제 링크
https://school.programmers.co.kr/learn/courses/30/lessons/68644

## 또 다른 풀이
```py
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
```