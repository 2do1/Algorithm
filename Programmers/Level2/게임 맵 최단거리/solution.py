from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    queue = deque()
    queue.append([x, y])
    width = len(maps[0]) # 가로 길이
    height = len(maps) # 세로 길이
    
    while queue: # 큐가 빌 때까지
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= height or ny >= width: # 맵을 벗어났을 경우
                continue
                
            if maps[nx][ny] == 0: # 벽이 있는 자리일 경우
                continue
            
            if maps[nx][ny] == 1: # 벽이 없는 자리일 경우
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])

    if maps[height - 1][width - 1] == 1: # 상대 팀 진영에 도달할 방법이 없을 경우
        return -1
    else: # 상대 팀 진영에 도달할 방법이 있을 경우
        return maps[height - 1][width - 1]
                
def solution(maps):
    answer = bfs(0, 0, maps) # 시작 지점
    
    return answer