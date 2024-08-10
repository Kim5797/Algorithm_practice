[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/258711)
## 문제
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들이 있습니다. 이 그래프들은 1개 이상의 정점과, 정점들을 연결하는 단방향 간선으로 이루어져 있습니다.

크기가 n인 도넛 모양 그래프는 n개의 정점과 n개의 간선이 있습니다. 도넛 모양 그래프의 아무 한 정점에서 출발해 이용한 적 없는 간선을 계속 따라가면 나머지 n-1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아오게 됩니다. 도넛 모양 그래프의 형태는 다음과 같습니다.
![alt text](image.png)

크기가 n인 막대 모양 그래프는 n개의 정점과 n-1개의 간선이 있습니다. 막대 모양 그래프는 임의의 한 정점에서 출발해 간선을 계속 따라가면 나머지 n-1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나 존재합니다. 막대 모양 그래프의 형태는 다음과 같습니다.
![alt text](image-1.png)

크기가 n인 8자 모양 그래프는 2n+1개의 정점과 2n+2개의 간선이 있습니다. 8자 모양 그래프는 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태의 그래프입니다. 8자 모양 그래프의 형태는 다음과 같습니다.
![alt text](image-2.png)

도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프가 여러 개 있습니다. 이 그래프들과 무관한 정점을 하나 생성한 뒤, 각 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 임의의 정점 하나로 향하는 간선들을 연결했습니다.
그 후 각 정점에 서로 다른 번호를 매겼습니다.
이때 당신은 그래프의 간선 정보가 주어지면 생성한 정점의 번호와 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야 합니다.

그래프의 간선 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다. 이때, 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 순서대로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## 필요한 생각
-- 그래프의 차이점
막대 그래프는 한줄이므로 사이클이 없음
도넛 그래프와 8자 그래프는 사이클이 생김
차이점은 도넛 모양 그래프는 한 노드를 중심으로 연결되어 있음
즉, 다시 돌아올때 다음에 새로운 노드가 있으면 8자그래프, 다음에 새로운 노드가 없으면 도넛 그래프

-- 새로 생성한 노드를 찾는 방법
다른 노드와 다르게 간선이 양쪽으로 뻗어 있음

-- 그래프를 구분하는 법
그 노드를 찾아서 없애고 각각으로 만들어지는 그래프를 구별하여 그래프의 종류를 판별하면 됨 

## 슈도 코드
def solution 함수(입력: 그래프의 간선 정보 edges[][])
    1. 방문 정보를 저장하는 리스트 visited[]를 edges의 요소 중 최대값의 크기로 False로 생성
    2. 그래프의 연결 정보를 저장할 리스트 graph[] 생성
    3. visited[]의 인덱스 node를 처음부터 끝까지 반복
        3-1. node가 null이 아닐때 까지 반복
            3-1-1. 

return 출력: [생성된 노드의 번호, 도넛 그래프의 개수, 막대 그래프의 개수, 8자 그래프의 개수]

## 또 다른 풀이
[링크1](https://trivia-starage.tistory.com/254)

```py
def solution(edges):
    answer = []
    max_node = 0
    for src, dst in edges:
        max_node = max(max_node, src, dst)
    
    indeg = [0] * (max_node + 1)
    outdeg = [0] * (max_node + 1)
    
    for src, dst in edges:
        indeg[dst] += 1
        outdeg[src] += 1
        
    gen_node = -1
    num_d, num_stick, num_eight = 0, 0, 0
    for i in range(1, max_node + 1):
        if indeg[i] == 0 and outdeg[i] >= 2:
            gen_node = i
        if indeg[i] > 0 and outdeg[i] == 0:
            num_stick += 1
        if indeg[i] >= 2 and outdeg[i] == 2:
            num_eight += 1
    num_d = outdeg[gen_node] - (num_stick + num_eight)
    
    answer = [gen_node, num_d, num_stick, num_eight]
    return answer
```

- 현재 풀이에 참고함
- 많은 풀이가 본 풀이와 구조가 비슷함

```py
# from 프로그래머스 by 신진철
from collections import deque

def solution(edges):
    answer = []
    maxv = -float('inf')  # maxv변수를 음의 무한대로 초기와하는 것
    
    # edges에서 가장 큰 값을 가져오는 부분
    # 즉, 노드의 개수를 알 수 있게 된다.
    # 이 부분은 max함수가 더 편할 수도....
    for i, j in edges:
        if i > j:
            if maxv < i:
                maxv = i
        else:
            if maxv < j:
                maxv = j


    center = []
    # 노드의 개수만큼 [0, 0]을 원소로 가지는 center리스트 생성
    for i in range(maxv):
        center.append([0, 0]) # in, out

    # edges에서 특정 노드가 나오는 빈도를 저장하는 부분
    # center의 0번째 열은 입구의 개수를 뜻함
    # center의 1번째 열은 출구의 개수를 뜻함
    for i, j in edges:
        center[i-1][1] += 1
        center[j-1][0] += 1

    # 입구의 개수가 0개이고 출구의 개수가 가장 많다면 그 노드가 새로 생성된 노드
    node = 0 # 생성된 노드 
    nodev = 0 
    for i in range(len(center)):
        if center[i][0] != 0:
            continue
        if center[i][1] > nodev:
            nodev = center[i][1]
            node = i
    node += 1
    answer.append(node)

    ## 도넛, 막대, 8자 모양을 판별하는 부분
    # 각 그래프의 개수를 저장하는 부분
    donut = 0
    stick = 0
    eight = 0
    # 방문 정보를 저장하는 visited변수. 
    visited = [False]*maxv # 노드의 개수의 크기만큼 생성함
    visited[node-1] = True # 생성된 노드는 방문으로 표시
    # 노드의 개수만큼 2차원 리스트 생성
    graph = [[] for _ in range(maxv)]
    startv = []
    
    for start, end in edges:
        if end == node:
            continue
        elif start == node:
            startv.append(end-1)
            continue
        graph[start-1].append(end-1)

    
    def bfs(start_v):
        """
        bfs(너비 우선 탐색)알고리즘
        """
        discovered = set()
        node = 0
        edge = 0
        stack = deque([start_v])
        while stack:
            v = stack.popleft()
            if v not in discovered:
                discovered.add(v)
                node += 1
                for w in graph[v]:
                    stack.append(w)
                    edge += 1
        return node, edge

    temp = []
    for i in startv:
        temp.append(bfs(i))

    for node, edge in temp:
        if node-1 == edge:
            stick += 1
        elif node == edge:
            donut += 1
        else:
            eight += 1

    answer.append(donut)
    answer.append(stick)
    answer.append(eight)

    return answer
```

```py
# from 프로그래머스 by goodchoi
import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

grp = []
def solution(edges):
    global grp

    grp = defaultdict(list)
    node_set = set()

    for edge in edges:
        start, end = edge
        grp[start].append(end)
        node_set.add(end)

    candidates = set(grp.keys()).difference(node_set)
    created_node = 0
    for candidate in candidates:
        if len(grp[candidate]) > 1:  # 임의 생성 노드는 항상 2개이상을 가지므로
            created_node = candidate

    grp_count = [0] * 3
    for start in grp[created_node]:
        visited = {start}
        grp_type = dfs(start, visited)
        grp_count[grp_type] += 1

    return [created_node,*grp_count]


def dfs(cur_v, visited):
    visited.add(cur_v)

    if cur_v not in grp:
        return 1

    if len(grp[cur_v]) > 1:
        return 2

    for next_v in grp[cur_v]:
        if next_v not in visited:
            result = dfs(next_v, visited)
            if result != 0:
                return result
    return 0


if __name__ == '__main__':
    solution(
        [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
         [11, 9], [3, 8]])
```
