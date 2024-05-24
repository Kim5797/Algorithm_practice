## 슈도 코드
```jsx
int function(int num){
    answer = 0 //반복 횟수를 저장하는 변수
    number = num //재귀호출이 아닌 변수의 변화로 알고리즘을 해결하기 위한 cache 변수

    1. 입력된 수가 1이면 0을 반환
    if (number == 1)
        return 0

    2. number이 1이 아닐 경우 반복하여 입력된 수를 판별하여 연산
    while number != 1 { 
        2-1. 입력된 수가 짝수라면 2로 나누고 횟수 +1. 
        if (number % 2 == 0)
            number = number / 2
            answer++
        2-2. 입력된 수가 홀수라면 3을 곱한 후 1을 더하고 횟수 +1.
        else if (number % 2 != 0)
            number = number * 3 + 1
            answer++    
        
        2-3. 횟수가 500회 이면 -1을 반환
        if (answer == 500)
            return -1
    }

    return answer
}
```