# is_total = int(input())
# count = int(input())

# real_total = 0

# for _ in range(count):
#     price, number = map(int, input().split())
#     real_total += price * number

# if is_total == real_total:
#     print("Yes")
# else:
#     print("No")

# chat에게 물어본 코드.
is_total = int(input())
count = int(input())

# 리스트 컴프리헨션을 사용하여 총합 계산
real_total = sum(price * number for price, number in (map(int, input().split()) for _ in range(count)))

# 결과 비교 및 출력
print("Yes" if is_total == real_total else "No")