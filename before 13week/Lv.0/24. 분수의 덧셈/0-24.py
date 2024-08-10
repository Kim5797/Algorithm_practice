import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer1 *= denom2
    numer2 *= denom1
    denom1 *= denom2
    answer.append(numer1 + numer2)
    answer.append(denom1)

    gcd = math.gcd(answer[0], answer[1])
    answer[0] //= gcd
    answer[1] //= gcd

    return answer