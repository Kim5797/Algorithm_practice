def solution(bandage, health, attacks):
    count = 0 # 연속으로 성공한 횟수
    current_health = health # 현재 체력
    current_time = 0 # 현재 시간

    for index in range(len(attacks)): #index = 0, 1, 2, 3
        for time in range(current_time, attacks[index][0] + 1): 
            if time == attacks[index][0]:
                current_time = time + 1
                current_health -= attacks[index][1]
                count = 0
                break
            if current_health > 0:
                if count < bandage[0]:
                    current_health += bandage[1]
                    count += 1
                    if count == bandage[0]:
                        current_health += bandage[2]
                        count = 0
                if current_health > health:
                    current_health = health
        if current_health <= 0:
            return -1


    return current_health

# Status: Accepted
bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(bandage, health, attacks)) 

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]

print(solution(bandage, health, attacks)) 