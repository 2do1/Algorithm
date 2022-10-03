from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start]) # 시작 노드 큐에 삽입
    visited[start] = True # 방문했다는 것을 처리

    while queue: # 큐가 빌때까지 계속 반복
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]: # 아직 방문하지 않은 노드일 경우
                queue.append(i) # 큐에 삽입
                visited[i] = True # 큐에 삽입 후 방문했다는 것을 처리


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

bfs(graph, 1, visited)