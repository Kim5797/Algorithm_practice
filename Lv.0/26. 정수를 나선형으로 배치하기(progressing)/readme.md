## 슈도 코드
```jsx
def solution (int n){
    answer = [[]]
    1. answer[0][0]부터 answer[0][n-1]까지 1 ~ n을 대입
    2. answer행렬에서 0부터 n*n - 1까지 순서대로 행 고정, 열 고정을 반복하여 1부터 n*n을 대입
        2-1. answer[row][col] = num
        //2-1. answer[0][n-1]부터 answer[n-1][n-1]까지 n ~ n + n-1을 대입
        //2-2. answer[n-1][n-1]부터 answer[n-1][0]까지 n + n-1 ~ (n + n-1) + n-1을 대입 
        //2-3. answer[n-1][0]부터 answer[n-1][1]까지
        
    for num in range(0, n**2):
        if row < n:
        

    return answer
}