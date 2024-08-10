## 문제 링크
https://school.programmers.co.kr/learn/courses/30/lessons/120923

## 또 다른 풀이
```py
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
```