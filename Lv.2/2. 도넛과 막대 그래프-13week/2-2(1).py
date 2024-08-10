def solution(edges):
    answer = [0] * 4
    graphs = edges
    visited = []
    queue = []

    # 각 입구의 수와 출구의 수를 기록
    in_degree = {}
    out_degree = {}
    for a, b in edges:
        out_degree[a] = out_degree.get(a, 0) + 1 # a의 출구 수를 1 증가
        in_degree[b] = in_degree.get(b, 0) + 1 # b의 입구 수를 1 증가
        in_degree.setdefault(a, 0)  # a가 없으면 0으로 초기화
        out_degree.setdefault(b, 0) # b가 없으면 0으로 초기화

    # 1. 생성된 노드 찾기
    for item in in_degree.items():
        if item[1] == 0 and out_degree[item[0]] >= 2:
            generated_node = item[0]
            answer[0] = generated_node
            break

    # 2. 막대, 도넛, 8자 그래프 찾기
    
    return answer

def dfs(edges, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(edges[node] - set(visited))
    return visited

def dfs_recursive(edges, start_node, visited=[]):
    visited.append(start_node)
    for node in edges[start_node] - set(visited):
        dfs_recursive(edges, node, visited)
    return visited
# edges에서 첫 번째 원소가 2인 원소를 찾는 코드
edges = [[1, 3], [2, 4], [2, 5], [3, 6]]  # 예제 2차원 배열
result = [edge for edge in edges if edge[0] == 2]  # 첫 번째 원소가 2인 원소를 찾음
print(result)  # 결과 출력