def solution(s):
    zero_count = 0
    remove_count = 0
    change_count = 0
    
    while s != str(bin(1))[2:]:
        zero_count += s.count('0')
        remove_count = s.count('0')
        ## 110이 저장되어야 한다. str로 .
        s = str(bin(len(s) - remove_count)[2:])  # 111111 6개
        change_count += 1
        
    answer = [change_count, zero_count]
    return answer


## 1. s에 0이 몇개인지 확인한다.
## 2. 0을 제외한 개수를 2진수로 바꾸어 s에 저장한다.
## 3. 0의 개수를 zero_count에 저장한다.
## 4. 이진 변환한 횟수를 change_count에 저장한다. 
## 5. 1~4를 s가 '1'이 될때 까지 반복한다.
## 6. [change_count, zero_count]으로 return한다.


## 1. s에 0이 몇개인지 확인한다.
## 2. 0을 제외한 개수를 2진수로 바꾸어 s에 저장한다.
## 3. 0의 개수를 zero_count에 저장한다.
## 4. 이진 변환한 횟수를 change_count에 저장한다. 
## 5. 1~4를 s가 '1'이 될때 까지 반복한다.
## 6. [change_count, zero_count]으로 return한다.


### test
print(solution("110010101001"))  # [3, 8]
print(solution("01110"))  # [3, 3]