def solution(board, h, w):
    answer = 0
    n = len(board)
    current_square = board[h][w]

    up = True
    down = True
    right = True   
    left = True

    if h == 0:
        up = False
    if h == n - 1:
        down = False
    if w == 0:
        right = False
    if w == n - 1:
        left = False
    
    if up is True:
        if board[h - 1][w] == current_square:
            answer += 1
    if down is True:
        if board[h + 1][w] == current_square:
            answer += 1
    if right is True:
        if board[h][w - 1] == current_square:
            answer += 1
    if left is True:
        if board[h][w + 1] == current_square:
            answer += 1    
    return answer


# The following is code to output testcase.
# board = [
#     [1, 2, 3],
#     [3, 2, 1],
#     [2, 1, 3]
# ]
# h = 1
# w = 1
board = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
h = 0
w = 0

print(solution(board, h, w)) # Expected output: 1