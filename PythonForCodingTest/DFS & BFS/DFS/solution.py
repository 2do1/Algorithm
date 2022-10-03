def dfs(graph, v, visited):
    visited[v] = True # 방문했다는 것을 처리
    print(v, end=' ')

    for i in graph[v]: # 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]: # 아직 방문하지 않은 노드일 경우
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)