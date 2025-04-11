# from collections import deque
# from sys import stdin

# def push(que, num):
#     que.append(num)

# def pop(que):
#     print(que.popleft() if que else -1)

# def size(que):
#     print(len(que))

# def empty(que):
#     print(0 if que else 1)

# def front(que):
#     print(que[0] if que else -1)

# def back(que):
#     print(que[-1] if que else -1)

# def process_command(que, command):
#     if command.startswith("push"):
#         _, num = command.split()
#         push(que, int(num))
#     elif command == "pop":
#         pop(que)
#     elif command == "size":
#         size(que)
#     elif command == "empty":
#         empty(que)
#     elif command == "front":
#         front(que)
#     elif command == "back":
#         back(que)

# N = int(stdin.readline().rstrip())
# que = deque()

# for _ in range(N):
#     order = stdin.readline().rstrip()
#     process_command(que, order)

from collections import deque
from sys import stdin

N = int(stdin.readline().rstrip())
que = deque()

for _ in range(N):
    order = stdin.readline().rstrip()

    if order[0:4] == "push":
        num = int(order.split()[1])
        que.append(num)
    elif order == "pop":
        print(que.popleft() if que else -1)
    elif order == "size":
        print(len(que))
    elif order == "empty":
        print(0 if que else 1)
    elif order == 'front':
        print(que[0] if que else -1)
    elif order == 'back':
        print(que[-1] if que else -1)