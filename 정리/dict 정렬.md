# dict를 정렬하는 법

- sorted를 사용한다.

- sort는 list의 메소드 이므로 사용할 수 없다.

- sort는 list 객체 자체를 수정한다. (혼란을 피하기 위해 None을 반환한다.)

- 그에 반해 sorted는 iterable 객체 자체를 수정하지 않고 그 객체를 정렬한 새로운 객체를 반환한다.

## 키를 기준으로 정렬

```py
a={'python':1, 'java':2, 'javascript':3, 'c':4}
sorted_dict = sorted(a.items())
```

## 키를 기준으로 정렬(키만 출력)

```py
a={'python':1, 'java':2, 'javascript':3, 'c':4}
sorted_dict = sorted(a)
```

## 값을 기준으로 정렬

```py
a={'python':1, 'java':2, 'javascript':3, 'c':4}
sorted_dict = sorted(a.items(), key = lambda x:x[1])
```
