
def solution(friends, gifts)
    다음달 선물 = list
    
    for A in friends (A는 자신)
        다음달 선물.append(0)
        for B in friends (B는 상대방)
            if A == B:
                다음으로 건너뛰기

            if A와 B가 선물을 주고받았다면
                if A가 B에게 선물을 더 많이 주었다면
                    A는 선물을 하나 받는다.
                elif B가 A에게 선물을 더 많이 주었다면
                    B는 선물을 하나 받는다.

            if A와 B가 선물을 주고 받지 않았다면 or A와 B가 선물을 주고받은 수가 같다면
                선물지수 = 자신이 친구들에게 준 선물의 수 - 자신이 친구들에게 받은 선물의 수
                if A의 선물지수가 B의 선물지수보다 크다면
                    A는 B에게 선물을 하나 받는다.
                elif B의 선물지수가 A의 선물지수보다 크다면
                    B는 A에게 선물을 하나 받는다.
                elif A의 선물지수와 B의 선물지수가 같다면
                    A와 B는 선물을 주고 받지 않는다.
    
    
    return 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수

