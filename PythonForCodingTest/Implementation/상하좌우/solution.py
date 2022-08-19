n = int(input()) # 공간의 크기
plan_list = input().split() # 이동할 계획서 내용

x, y = 1, 1 # 시작 지점
dx = [-1, 1, 0, 0] # 상하좌우 순서
dy = [0, 0, -1, 1]
command_list = ['U', 'D', 'L', 'R'] # 각 문자

for plan in plan_list:
    for i in range(len(command_list)):
        if plan == command_list[i]: # 각 문자마다 이동 수행
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간을 벗어났을 경우 움직임 무시
        continue

    x, y = nx, ny # 이동 수행

print(x, y) # 도착 지점 좌표 출력