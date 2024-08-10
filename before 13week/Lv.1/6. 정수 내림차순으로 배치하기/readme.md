```jsx
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
```
## 슈도 코드
```jsx
def solution(n):
    answer = 0
    list(map(int, str(n)))
    list = list.sort()
    answer = int(list)
    return answer 
```
```jsx
join 사용법
'구분자'.join(리스트)
리스트에서 구분자를 기준으로 원소들을 합치는 함수
```

