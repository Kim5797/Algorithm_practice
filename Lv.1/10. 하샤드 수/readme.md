# 슈도 코드
```jsx
1. sum의 속도를 늘리기 위해 numpy 모듈 불러오기(출처: https://ctkim.tistory.com/entry/Python-Sum-function)
function (int number){
    
    2. number를 각 자릿수를 리스트로 저장
    for num in (0, number, +1){
        리스트에 num을 하나씩 저장
    } 

    3. 리스트의 모든 요소의 합 구하기
    합 = numpy.sum(리스트)
    
    4. number를 합으로 나누어 떨어지는지 확인
    if number % 합 == 0
        answer = ture 
    else 
        answer = false

    return answer = bool
}
```
---
# 또 다른 풀이
```jsx
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0
```
## 문제 설명
* for 문법과 관련된 삼항연산자 사용
```jsx
for num in (str(x)):
    num_list.append(int(num))
```
부분을
```jsx
int(x) for x in str(n))
```
으로 풀이함

* n을 str으로 수정 후 이를 하나씩 반복하여 int형의 리스트로 변경함
---

