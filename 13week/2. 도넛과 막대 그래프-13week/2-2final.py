def solution(edges):
    donut = 0
    stick = 0
    eight = 0

    # 각 입구의 수와 출구의 수를 기록
    in_degree = {}
    out_degree = {}
    for a, b in edges:
        out_degree[a] = out_degree.get(a, 0) + 1 # a의 출구 수를 1 증가
        in_degree[b] = in_degree.get(b, 0) + 1 # b의 입구 수를 1 증가
        in_degree.setdefault(a, 0)  # a가 없으면 0으로 초기화
        out_degree.setdefault(b, 0) # b가 없으면 0으로 초기화

    # 새로 생성된 노드 판별
    for item in in_degree.items():
        if item[1] == 0 and out_degree[item[0]] >= 2:
            generated_node = item[0]
        if item[1] >= 1 and out_degree[item[0]] == 0:
            stick += 1
        if item[1] >= 2 and out_degree[item[0]] == 2:
            eight += 1

    donut = out_degree[generated_node] - (stick + eight)

    return [generated_node, donut, stick, eight]