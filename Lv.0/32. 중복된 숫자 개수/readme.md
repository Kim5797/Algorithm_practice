## 내 풀이
```py
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer
```

## 또 다른 풀이
```py
def solution(array, n):
    return array.count(n)
```

### count 함수
count함수는 특정 배열이나 컬렉션의 요소 수를 반환하는 함수이다. 