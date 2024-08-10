## 문제 링크
https://school.programmers.co.kr/learn/courses/30/lessons/12912

## 슈도 코드
def solution(정수 a,정수 b):
    만약 a가 b보다 작으면:
        a에서 1씩 커가며 b까지 더함
    만약 b가 a보다 작으면:
        b에서 1씩 커가며 a까지 더함
    만약 a와 b가 같다면:
        a를 출력해야 함

## 또 다른 풀이
```py
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
```