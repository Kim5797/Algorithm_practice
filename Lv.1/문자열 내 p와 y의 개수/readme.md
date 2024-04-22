```jsx
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
```

## 생각 과정
문자열에서 'p'의 개수를 읽고 'y'의 개수 만큼 빼서 
0이면 같은 개수가 있는 것이므로 True
0이 아니면 다른 개수가 있는 것이므로 False를 출력

## 코드 과정
```jsx
def 결과(입력: string)
    count를 0으로 초기화
    반복 (string의 한 요소씩, 처음부터, 끝까지)
        만약 char == 'p' 이면
            count += 1
        만약 char == 'y' 이면
            count -= 1
        
    만약 count == 0 이면
        answer = True
    아니라면
        answer = False
    return answer
```

## 시도 1
```jsx
def solution(s):
    answer = True
    count = 0
    
    for char in s:
        if char == 'p':
            count += 1
        elif char == 'y':
            count -= 1

    if count == 0:
        answer = True
    else:
        answer = False
    
    return answer
```
실패 요인:


문제 조건의 "대문자와 소문자를 구별하지 않는다." 부분을 고려하지 않음

## 시도 2
```jsx
def solution(s):
    answer = True
    count = 0
    
    for char in s:
        char = char.lower()
        if char == 'p':
            count += 1
        elif char == 'y':
            count -= 1

    if count == 0:
        answer = True
    else:
        answer = False
    
    return answer
```
성공
