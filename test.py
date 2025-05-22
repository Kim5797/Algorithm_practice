팀_선호도 = [1, 2, 3]
팀_선호도.remove(1)
팀_선호도 = list(map(lambda x: x - 1, 팀_선호도))
print(팀_선호도)