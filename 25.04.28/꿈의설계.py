# https://pyalgo.co.kr/?page=4
import re

data = ['100만큼 A를 훈련. 201 B. 120보다 이십만큼 더 B를 훈련했다.', 
        '30만큼 A를 고민했다. 40만큼 B를 고민. 빙키는 A를 70만큼. C 10. D 10. A 10. z 10.']

def solution(data):
    훈련수치, 고민수치 = data

    훈련수치 = 훈련수치.split('.')
    고민수치 = 고민수치.split('.')

    수치패턴 = re.compile(r'(\d{1,3})')
    문자패턴 = re.compile(r'([a-zA-Z])')

    훈련dict = {}
    고민dict = {}

    원래미래 = 0
    바뀐미래 = 0

    # 훈련수치
    for i in 훈련수치[:-1]:
        a = 문자패턴.search(i)
        b = 수치패턴.search(i)
        if a.group() not in 훈련dict:
            훈련dict[a.group()] = int(b.group())
        else:
            훈련dict[a.group()] += int(b.group())

    # 고민수치치
    for i in 고민수치[:-1]:
        b = 수치패턴.search(i)
        a = 문자패턴.search(i)
        if a.group() not in 고민dict:
            고민dict[a.group()] = int(b.group())
        else:
            고민dict[a.group()] += int(b.group())

    # 원래 미래
    for i in 훈련dict.keys():
        if i in 고민dict:
            원래미래 += 훈련dict[i] * 고민dict[i]

    if 원래미래 == 0:
        return '미래가 보이지 않습니다.'

    # 바뀐미래
    훈련수치중가장큰값 = max(훈련dict.values())
    고민수치중가장큰값 = max(고민dict.values())

    for i in 훈련dict:
        if 훈련dict[i] == 훈련수치중가장큰값:
            훈련dict[i] += 100

    for i in 고민dict:
        if 고민dict[i] == 고민수치중가장큰값:
            고민dict[i] += 100

    for i in 훈련dict.keys():
        if i in 고민dict:
            바뀐미래 += 훈련dict[i] * 고민dict[i]
    
    return f'최종 꿈의 설계는 원래 미래 {원래미래}, 바뀐 미래 {바뀐미래}입니다. 이 수치대로 Vision을 만듭니다.'