## 문제링크

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/120849/solution_groups?language=python3)

## 또 다른 풀이

```py
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
```

```py
import re

def solution(my_string):
    return re.sub(r"a|e|i|o|u", "", my_string)
```

## 참조할만한 사이트

https://seoulitelab.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0%ED%95%98%EB%8A%94-3%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95