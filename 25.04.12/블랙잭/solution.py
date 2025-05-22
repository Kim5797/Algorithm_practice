from itertools import combinations

def find_black_jack(field_card, M):
    max_sum = 0
    for cards in combinations(field_card, 3):
        current_sum = sum(cards)
        if current_sum <= M:
            max_sum = max(max_sum, current_sum)
    return max_sum
    
            

N, M = map(int, input().split())
field_card = list(map(int, input().split()))

print(find_black_jack(field_card, M))