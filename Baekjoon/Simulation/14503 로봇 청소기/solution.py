n, m = map(int, input().split())

r, c, d = list(map(int, input().split())) # (r,c) 좌표, d 방향
areas = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)] # 방문 표시

# 북 동 남 서
# 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0 # 작동을 멈출 때까지 청소하는 칸의 개수

# 현재 위치 청소 및 카운팅
visited[r][c] = True
areas[r][c] = 2
answer += 1

x, y = r, c # 현재 청소기 위치의 좌표
while True:

    all_clear = True # 네칸이 모두 다 청소되었는지의 여부
    for _ in range(4):
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전

        nx = x + dx[d] 
        ny = y + dy[d]

        # 범위에 벗어나지 않았을 경우, 청소되지 않은 빈칸일 경우, 방문하지 않았을 경우
        if 0 <= nx < n and 0 <= ny < m and areas[nx][ny] == 0 and not visited[nx][ny]: 
            visited[nx][ny] = True
            areas[nx][ny] = 2 # 청소했다는 표시
            x = nx
            y = ny 

            all_clear = False # 네 칸이 모두 청소되지 않았을 경우에 
            answer += 1
            break
    
    if all_clear: # 네 칸이 모두 청소되었을 경우
        # 현재 바라보는 방향의 반대 방향
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4] 

        if 0 <= nx < n and 0 <= ny < m and areas[nx][ny] == 1: # 후진하였을 때 벽일 경우
            break 
        
        # 후진할 수 있을 경우 후진 위치로 이동
        x = nx
        y = ny
            
print(answer)