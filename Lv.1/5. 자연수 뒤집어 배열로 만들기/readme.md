```jsx
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
```

## 슈도코드
```jsx
solution(입력: n)
    리스트형 변수 array 생성
    array <= n을 문자열로 변환
    array의 원소를 거꾸로 변환
    for num in (array의 원소)
        answer에 int(num)을 하나씩 저장
    return answer
```