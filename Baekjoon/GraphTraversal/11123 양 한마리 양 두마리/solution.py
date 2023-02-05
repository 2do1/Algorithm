import sys
sys.setrecursionlimit(50000)

def dfs(x, y):

    if x >= h or x < 0 or y >= w or y < 0:
        return False
    
    if not visited[x][y] and graph[x][y] == "#":
        visited[x][y] = True
        # 상하좌우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    
    return False

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    graph = [input() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == "#":
                dfs(i, j)
                answer += 1

    print(answer)