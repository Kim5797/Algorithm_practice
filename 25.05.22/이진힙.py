T = int(input())

# 힙 트리 구조
# struct{heap = [0, 값1(루트), 값2, ...]; heap_size = int()}(인덱스가 노드 주소. 노드가 비어있으면 None)
# - 삽입(최소 힙)
# 새로운 노드를 마지막 노드에 넣고 부모가 작으면 위에 올림
# 부모 노드: int(i/2)
for test_case in range(1, T + 1):
    max_heap_size = int(input())
    heap_size = 0
    input_number = map(int, input().split())
    
    last_node = 0
    heap = [0]
    # 삽입
    for num in input_number:
        heap.append(num)
        heap_size += 1
        
        # 루트 노드 추가 시 다음 연산으로 넘어감
        if heap_size == 1:
            continue
        
        # 현재 노드와 그 부모 노드의 index 연산
        now_index = heap_size
        parents_index = int(now_index/2)
        
        # 삽입 후 정리 부분
        while num < heap[parents_index]: # num이 부모 노드보다 작을 경우까지
            # 부모와 자식을 변경
            heap[parents_index], heap[now_index] = heap[now_index], heap[parents_index]
            now_index = parents_index
            # now_index가 루트에 해당하는 1이면 정리할 필요가 없음
            if now_index == 1:
                break
            else:
                parents_index = int(now_index/2)
            # num이 부모보다 크거나 같으면 정리할 필요 없음
            
    # 조상 노드 합 찾기
    # 가장 끝 조상은 항상 루트이므로 조사중인 index가 1이면 break
    last_node = heap[heap_size]
    ancestor_sum = 0
    now_index = heap_size
    parents_index = (int(now_index/2) if now_index != 1 else None)
    
    while now_index != 1:
        ancestor_sum += heap[parents_index]
        now_index = parents_index
        parents_index = int(now_index/2)
        
    print(f'#{test_case} {ancestor_sum}')