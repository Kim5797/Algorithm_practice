# https://pyalgo.co.kr/?page=3

data = [['A', 25, 24, 11, 12], ['B', 13, 22, 16, 14]]

def solution(data):
    전체인원수 = len(data)
    
    if 0 <= 전체인원수 <= 2:
        return []
     
    선발해야하는인원수 = int(전체인원수 * 30/100)

    if 선발해야하는인원수 == 0:
        return []
    
    선발된인원 = 0
    선발인원리스트 = []
    점수dict = {} # 점수 : [이름,?]

    for i in data:
        합 = sum(i[1:])
        if 합 in 점수dict:
            점수dict[합] += [i[0]]
        else:
            점수dict[합] = [i[0]]

    for i in sorted(list(점수dict.items()), reverse = True):
        if 선발된인원 < 선발해야하는인원수 and len(i[1]) <= 선발해야하는인원수 - 선발된인원:
            선발인원리스트.extend(i[1])
            선발된인원 += len(i[1])
        elif len(i[1]) > 선발해야하는인원수:
            return sorted(선발인원리스트, reverse = True)
        
    return sorted(선발인원리스트, reverse = True)

print(
    solution([['A', 25, 24, 11, 12], ['B', 13, 22, 16, 14]]) == []
) 

print(
    solution([['A', 11, 23, 17, 15], ['B', 15, 22, 17, 22], ['C', 13, 22, 16, 14], ['D', 18, 22, 16, 25], ['E', 8, 13, 23, 21]]) == ['D']
) 

print(
    solution([['A', 25, 25, 25, 25], ['B', 25, 25, 25, 25], ['C', 25, 25, 25, 25], ['J', 13, 22, 16, 14]]) == []
) 