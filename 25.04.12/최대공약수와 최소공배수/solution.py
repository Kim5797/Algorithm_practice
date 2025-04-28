def GCD(num_1,num_2):
    r = 0

    if num_1 == num_2:
        return num_1
    elif num_1 > num_2:
        while True:
            r = num_1 % num_2
            if r == 0:
                return num_2
            num_1, num_2 = num_2, r
    else:
        while True:
            r = num_2 % num_1
            if r == 0:
                return num_1
            num_2, num_1 = num_1, r

def LCM(num_1, num_2):
    return num_1*num_2 // GCD(num_1, num_2)


num_1, num_2 = map(int, input().split())
print(GCD(num_1, num_2))
print(LCM(num_1, num_2))
