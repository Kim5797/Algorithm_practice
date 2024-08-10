def solution(friends, gifts):
    chart = [[0 for col in range(len(friends))] for row in range(len(friends))]
    # chart = [[0, 0, 0, 0], 
    #          [0, 0, 0, 0], 
    #          [0, 0, 0, 0], 
    #          [0, 0, 0, 0]]
    next_gift = [0 for col in range(len(friends))]
    gift_give = list()
    gift_take = list()
    index = 0
    for gift in gifts: #준 사람과 받음 사람에 대한 리스트 생성
        gift_give.append(gift.split(' ')[0])
        # gift_give = {"muzi", "muzi", "ryan", "ryan", "ryan", "frodo", "frodo", "neo"}
        gift_take.append(gift.split(' ')[1]) 
        # gift_take = {"frodo", "frodo", "muzi", "muzi", "muzi", "muzi", "ryan", "muzi"}

    for i,friend in enumerate(gift_give): #준 사람에 대한 표 작성
        # print(i, friend)
        # print(friends.index(friend), friends.index(gift_take[i]))
        chart[friends.index(friend)][friends.index(gift_take[i])] += 1 #준 사람의 표에 받은 사람에 대한 표를 1씩 증가
    # chart = [[0, 0, 2, 0], 
    #          [3, 0, 0, 0], 
    #          [1, 1, 0, 0], 
    #          [1, 0, 0, 0]]

    gift_give_factor = [0 for col in range(len(friends))]
    gift_take_factor = [0 for col in range(len(friends))]
    gift_factor = [0 for col in range(len(friends))]
    
    for row in range(len(chart)):
        for col in range(len(chart[0])):
                gift_give_factor[row] += chart[row][col]
                gift_take_factor[col] += chart[col][row]
                gift_factor[row] += chart[row][col] - chart[col][row]
    # gift_give_factor = [2, 3, 2, 1]
    # gift_take_factor = [5, 1, 2, 0]
    # gift_factor = [-3, 2, 0, 1]
    # chart = [[0, 0, 2, 0],
    #          [3, 0, 0, 0],
    #          [1, 1, 0, 0],
    #          [1, 0, 0, 0]]
    for A in range(len(friends)):
        print(next_gift)
        for B in range(len(friends)):
            if A == B:
                continue
            elif chart[A][B] > chart[B][A]:
                next_gift[A] += 1
            elif chart[A][B] < chart[B][A]:
                next_gift[B] += 1
            elif chart[A][B] == chart[B][A]:
                if gift_factor[A] > gift_factor[B]:
                    next_gift[A] += 1
                elif gift_factor[A] < gift_factor[B]:
                    next_gift[B] += 1
    next_gift.sort(reverse=True)
    print(int(next_gift[0] / 2))

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

solution(friends, gifts)