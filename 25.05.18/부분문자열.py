T = int(input())

# suffix automaton 사용
class State:
    def __init__(self):
        self.length = 0
        self.transitions = {}
        self.link = -1
        self.count = 0

def build_suffix_automaton(string):
    automaton = [State()]
    last = 0

    for c in string:
        current = len(automaton)
        automaton.append(State())
        automaton[current].length = automaton[last].length + 1

        p = last
        while p != -1 and c not in automaton[p].transitions:
            automaton[p].transitions[c] = current
            p = automaton[p].link

        if p == -1:
            automaton[current].link = 0
        else: # 링크를 다음으로 넘기는 부분
            q = automaton[p].transitions[c]
            if automaton[p].length + 1 == automaton[q].length:
                automaton[current].link = q
            else:  # 클론 생성
                clone = len(automaton)
                automaton.append(State())
                automaton[clone].length = automaton[p].length + 1
                automaton[clone].transitions = automaton[q].transitions.copy()
                automaton[clone].link = automaton[q].link
            
                while p != -1 and automaton[p].transitions.get(c) == q:
                    automaton[p].transitions[c] = clone
                    p = automaton[p].link
                
                automaton[q].link = automaton[current].link = clone
        
        last = current
    
    for i in range(len(automaton)):
        automaton[i].count = 1

    states = sorted(range(1, len(automaton)), key = lambda x: automaton[x].length)
    for i in states:
        if automaton[i].llink != -1:
            automaton[automaton[i].link].count += automaton[i].count

    return automaton

def find_nth_substring(automaton, N):
    visited = [False] * len(automaton)
    substring = ""
    count = 0
    
    def dfs(state, current_str):
        nonlocal count, substring
        visited[state] = True
        
        # 사전순으로 전이 정렬
        transitions = sorted(automaton[state].transitions.items())
        for char, next_state in transitions:
            if count == N - 1:
                substring = current_str + char
                return True
            
            count += 1
            if not visited[next_state]:
                if dfs(next_state, current_str + char):
                    return True
        
        return False
    
    dfs(0, "")  # 초기 상태에서 시작
    
    if substring:
        return substring[0], len(substring)  # 첫 글자와 길이 반환
    return None, None  # N이 전체 부분 문자열 수보다 큰 경우

for test_case in range(1, T + 1):
    N, S = input().split()
    N = int(N)

    suffixes = [(S[i:], i) for i in range(len(S))]
    suffixes.sort()

    lcp = [0] * len(suffixes)
    for i in range(1, len(suffixes)):
        prev, _ = suffixes[i-1]
        curr, _ = suffixes[i]
        j = 0
        while j < min(len(prev), len(curr)) and prev[j] == curr[j]:
            j += 1
        lcp[i] = j

    count = 0
    for i in range(len(suffixes)):
        suffix, original_i = suffixes[i]
        unique_substrings = len(suffix) - (lcp[i] if i > 0 else 0)
        if count + unique_substrings >= N:
            pos = N - count - 1 + (lcp[i] if i > 0 else 0)
            first_char, length = suffix[0], pos + 1
            break
        count += unique_substrings

    print(f'#{test_case} {first_char} {length}')

    # # suffix automaton 활용
    # N, S = input().split()
    # N = int(N)

    # automaton = build_suffix_automaton(S)
    # first_char, length = find_nth_substring(automaton, 3)
    # print(f'#{test_case} {first_char} {length}')

    # # 직접 탐색 방법.
    # N, S = input().split()
    # N = int(N)
    # 부분S = set()
    # len_S = len(S)

    # for i in range(len_S):
    #     for j in range(i + 1, len_S+1):
    #         부분S.add(S[i:j])


    # # print(sorted(부분S))
    # 부분S = sorted(set(부분S))
    # answer = 부분S[N - 1]
    # print(f'#{test_case} {answer[0]} {len(answer)}')
    # # print(sorted(S))