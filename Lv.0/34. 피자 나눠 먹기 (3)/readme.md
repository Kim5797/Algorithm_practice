## 내 풀이

```py
def solution(slice, n):
    if n%slice == 0:
        return n//slice
    else:
        return n//slice + 1
```

## 또 다른 풀이

```py
def solution(slice, n):
    return (n-1)//slice + 1
```