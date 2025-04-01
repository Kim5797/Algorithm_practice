max_number = 0
index = 0
max_index = 0

for _ in range(9):
    input_number = int(input())
    index += 1
    
    if max_number < input_number:
        max_number = input_number
        max_index = index

print(f'{max_number} \n{max_index}')
