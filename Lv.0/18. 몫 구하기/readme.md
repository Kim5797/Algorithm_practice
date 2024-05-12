```jsx
문제 설명
정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
```
---
```jsx
또 다른 풀이
solution = int.__floordiv__
```
---
```jsx
__floordiv__ 메소드
python의 내장 메소드로 두 수의 몫을 구하는 데 사용된다.
이 메소드는 몫 연산자를 사용할 때 호출되며, 소수점 이하를 버리고 정수 부분만 반환한다.
```
---
```jsx
그 외의 연산을 위한 특수 메서드
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()
```
