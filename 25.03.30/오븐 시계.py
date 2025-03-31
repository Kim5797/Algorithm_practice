h, m = map(int, input().split())
oven_time = int(input())

if oven_time >= 60:
    oven_h, oven_m = divmod(oven_time, 60)
    h += oven_h

else:
    oven_m = oven_time

m += oven_m
if m >= 60:
    h += 1
    m -= 60

if h >= 24:
    h %= 24

print(f'{h} {m}')
    

# oven_time이 60 이상인지 확인
#   60으로 나눈 몫(시간, oven_h)과 나머지(분, oven_m)을 따로 저장
#   oven_h을 h에 더함
#   만약 h가 23을 넘어가면 
#       h를 23으로 나누어 나머지만 h로 저장
# 아니면
#   oven_time을 oven_m으로 저장
#   
# m에 oven_m을 더함
# 만약 m이 60 이상이면
#   h에 1 더함
#   m에 60을 뺌