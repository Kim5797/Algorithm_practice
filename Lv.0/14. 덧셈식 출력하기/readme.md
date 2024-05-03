## 또 다른 풀이
'''jsx
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")
'''
f스트링을 사용한 포맷팅

'''jsx
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))
'''
format()함수를 사용한 포맷팅