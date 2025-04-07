N = int(input())
l = ''
S = []
for num in range(N-1, 0, -1):
    l = l + ' ' * num
    l = l + '*' * (2 * (N - num) - 1)
    print(l)
    if num != 0:
        S.append(l)

    l = ''
    
for i in range(N - 1):
    print(S)
    # print(S.pop())    
    
# N이 들어왔을 때
# N번을 반복, index가 N-1에서 0인 부분에 각각 1, 3, 5, ... 2N-1까지의 숫자를 출력
# 여기서 N - 1까지의 출력 내용을 list에 저장.
# 위의 반복이 끝나면 N-1번 list에서 pop하여 출력한다.