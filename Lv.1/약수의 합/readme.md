```jsx
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
```

## 생각 과정
약수는 자기 자신이 최대.
즉, 1부터 자기 자신까지의 수 중 나누었을 때 나머지가 0이라면 
n은 그 수를 약수로 가진다.

## 코드 과정
```jsx
def 결과(입력: n)
    결과값을 0으로 초기화
    for num in 1부터 n까지
        만약 n을 num으로 나누었을때 나머지가 0이라면
            결과값 += num
    return answer
```

## 시도 1
```jsx
def solution(n):
    answer = 0
    for num in range(n): #오류 발생
        if n % num == 0:
            answer += num
    return answer
```
실패 요인:
ZeroDivisionError의 경우를 고려하지 않음
여기서 range함수의 기능을 잊어서 다시 찾아봄

## 시도 2
```jsx
def solution(n):
    answer = 0
    for num in range(1, n + 1):
        if n % num == 0:
            answer += num
    return answer
```
성공
