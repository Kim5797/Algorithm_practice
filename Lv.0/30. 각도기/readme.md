## 또 다른 풀이
```py
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
```