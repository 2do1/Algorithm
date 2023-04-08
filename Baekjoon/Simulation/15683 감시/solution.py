import copy

def monitor(x, y, directions, room_copy):

    for direction in directions:
        nx = x
        ny = y

        while True:
            nx += dx[direction]
            ny += dy[direction]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or room_copy[nx][ny] == 6:
                break

            if room_copy[nx][ny] == 0:
                room_copy[nx][ny] = '#'

    
def dfs(depth, room):
    global answer

    if depth == len(cctvs): # 각 케이스를 다 골랐을 경우
        total_zero = 0 
        for row in room: # 사각지대 카운팅
            total_zero += row.count(0)
        
        answer = min(answer, total_zero)
        return

    room_copy = copy.deepcopy(room)
    cctv_x, cctv_y, cctv_num = cctvs[depth]
    for directions in case[cctv_num]:
        monitor(cctv_x, cctv_y, directions, room_copy)
        dfs(depth + 1, room_copy)
        room_copy = copy.deepcopy(room)


n, m = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

# CCTV 방향에 있는 칸 전체 감시 가능
# 벽은 통과 X, CCTV는 CCTV를 통과할 수 있다.
# CCTV 90도 방향으로 회전 가능

cctvs = [] # cctv의 좌표들
for x in range(n):
    for y in range(m):
        if 1 <= room[x][y] <= 5:
            cctvs.append([x, y, room[x][y]]) # CCTV 좌표랑 CCTV 번호 넣어둔다.

# 12시부터 시계방향으로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 카메라당 가능한 경우의수
case = [
    [],
    [[0], [1], [2], [3]], # 1번 카메라
    [[0, 2], [1, 3]], # 2번 카메라
    [[0, 1], [1, 2], [2, 3], [0, 3]], # 3번 카메라
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 카메라
    [[0, 1, 2, 3]] # 5번 카메라
]

answer = 2e9 # 사각 지대의 최소 크기
dfs(0, room)
print(answer)