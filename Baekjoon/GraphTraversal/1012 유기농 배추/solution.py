import sys
sys.setrecursionlimit(5000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # 밖으로 벗어날 경우
        return False
    
    if graph[x][y] == 1: # 배추일 경우
        graph[x][y] = -1 # 방문표시 해준다

        # 상하좌우로 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    
    return False

t = int(input()) # 테스트케이스의 개수

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로 m, 세로 n, 배추 심어져 있는 위치 개수 k
    graph = [[0] * m for _ in range(n)] # 땅
    answer = 0 # 최소의 배추흰지렁이 마리 수 

    for _ in range(k):
        x, y = map(int, input().split()) # 배추 위치
        graph[y][x] = 1 # 땅에 배추 표시
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j): 
                answer += 1 
    
    print(answer)