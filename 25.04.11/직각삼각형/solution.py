length = []

while True:
    length = list(map(float, input().split()))
    if length == [0.0, 0.0, 0.0]:
        break
    
    max_length = max(length)
    length.remove(max_length)
    if max_length**2 == length[0]**2 + length[1]**2:
        print('right')
    else:
        print('wrong')