from collections import deque

t = int(input()) # 테스트 케이스의 개수

# 나이트가 한 번에 이동할 수 있는 칸
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append([x1, y1])

    while queue: # 큐가 빌 때 까지
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l: # 맵 밖을 벗어 났을 경우
                continue
            
            if graph[nx][ny] == 0: # 이동할 수 있는 칸일 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    
    return graph[x2][y2]

for _ in range(t):
    l = int(input()) # 체스판 한 변의 길이
    x1, y1 = map(int, input().split()) # 나이트가 현재 있는 칸
    x2, y2 = map(int, input().split()) # 나이트가 이동하려고 하는 칸

    graph = [[0] *  l for _ in range(l)] # 체스판

    if x1 == x2 and y1 == y2: # 이동을 안해도 될 경우
        answer = 0
    else:
        answer = bfs(x1, y1, x2, y2) 
    print(answer)