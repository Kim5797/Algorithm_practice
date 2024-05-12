```jsx
문제 설명
정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
```
---
```jsx
또 다른 풀이
def solution(num1, num2):
    return divmod(num1, num2)[1]
```
---
```jsx
divmod(x, y)
두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다.  
__builtin__ module에 포함된 function 이다. 
출처: https://technote.kr/259 [TechNote.kr:티스토리]
```