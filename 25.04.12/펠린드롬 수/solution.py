def is_Palindrome(parameter):
    max_index_of_parameter = len(parameter) - 1
    this_is_Palindrime = True

    for index, char in enumerate(parameter):
        if char != parameter[max_index_of_parameter - index]:
            return 'no'
        
    return 'yes'
while True:
    number = input()
    if number == '0':
        break
    
    print(is_Palindrome(number))