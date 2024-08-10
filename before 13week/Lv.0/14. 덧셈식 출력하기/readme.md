## 또 다른 풀이


## f스트링을 사용한 포맷팅
```jsx
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")
```
## format()함수를 사용한 포맷팅
```jsx
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))
```
