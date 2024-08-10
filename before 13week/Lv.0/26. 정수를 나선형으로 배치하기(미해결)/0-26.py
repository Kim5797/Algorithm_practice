def solution(n):
    answer = [[None] * n for _ in range(n)]
    row = 0
    col = 0
    
    for num in range(1, n**2 + 1):
        if num <= n:
            answer[row][col] = num
            row += 1
            col = 0
            continue
        else:
            row += 1
                
        
        if row == n - 1 and col == n - 1:
            row = n - 1
            col -= 1
        
        if row == 0 and col == n - 1:
            


    return answer
solution(4)