original_status_of_chess = (1, 1, 2, 2, 2, 8)

Found = map(int, input().split())

needed = [original - found for original, found in zip(original_status_of_chess, Found)]

print(" ".join(map(str, needed)))