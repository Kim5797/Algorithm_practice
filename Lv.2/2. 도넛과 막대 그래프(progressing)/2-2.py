
def solution(edges):
    donut_count = 0
    eight_count = 0
    line_count = 0 
    visited = [False] * max(map(max, edges))
    graph = []

    for current_node, next_node in edges:
        if edges.
    

    return [donut_count, eight_count, line_count]

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges)) # [1, 3, 4]


class graph_Algorithm: # 그래프 알고리즘 클래스
    graph = [] # 그래프
    seperated_graph = [] # 분리된 그래프
    graph_size = 0 # 그래프 크기
    new_node = 0 # 새로운 노드

    def __init__(self, edges):
        self.graph_size = max(map(max, edges))
        self.graph_to_list(edges) # 그래프 리스트로 변환
        self.delete_node() # 노드 삭제

    def graph_to_list(self, edges):
        self.graph = list([] for _ in range(max(map(max, edges))))
        
        for start_node, end_node in edges:
            self.graph[start_node].append(end_node)

    def delete_node(self):
        for index in range(self.graph_size):
            if len(self.graph[index]) >= 2:
                self.graph[index] = []
                new_node = index + 1
                break
        
        # for index in range(self.graph_size):
        #     if new_node in self.graph[index]:
        #         self.graph[index].remove(new_node)

    def seperating_graph(self):
        from collections import deque
        visited = []
        need_visited = deque()

        for index in range(self.graph_size):
            start_node = index
            visited.clear()
            need_visited.clear()
            


        
        
##### example
# edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
# graph = [[1], [3, 1], [], [3]]
# seperated_graph = [[1], [], [], [3]]
                
# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], 
#          [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], 
#          [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]	
# graph = [[12], [], [5, 8], [2, 8, 11], [3], [10], 
#          [11], [3], [6], [11], [1, 9], [7]]
# seperated_graph = [[12], [], [5, 8], [], [3], [10],
#                    [11], [3], [6], [11], [1, 9], [7]]
            


# example
# edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]


# class graph_Algorithm: # 그래프 알고리즘 클래스
#     visited = [] # 노드 방문 여부
#     graph = [] # 그래프
#     def __init__(self, graph):
#         self.graph = graph
#         self.vistied.clear()

#     def DFS(self):
#         for vertex in self.graph:
#             self.visited.append(False)
#         for vertex in self.graph:
#             if not self.visited[vertex]:
#                 self.DFS_recursive(vertex)

#     def DFS_recursive(self, vertex):
#         self.visited[vertex] = True
#         print(vertex)
#         for adjacent in self.graph[vertex]:
#             if not self.visited[adjacent]:
#                 self.DFS_recursive(adjacent)
