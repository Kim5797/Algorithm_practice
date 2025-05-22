# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    answer = ''

    temp_N = N * 2
    while len(answer) <= 12:
        integar, back_float_point = str(temp_N).split('.')
        answer += integar
        if int(back_float_point) == 0:
            break
        else:
           temp_N = float(f'0.{back_float_point}')
        temp_N = temp_N * 2

    if len(answer) >= 13:
        print('overflow')
    else:
        print(f'#{test_case} {answer}')
    