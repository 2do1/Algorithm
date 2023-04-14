def solution(dirs):
    answer = 0
    
    directions = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]} # 방향 저장
    
    visited = [[]]
    
    x, y, = 0, 0 # 0, 0 위치에 시작
    
    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5: # 맵 밖을 벗어 나지 않았을 경우
            if [x, y, nx, ny] not in visited and [nx, ny, x, y]:                 
                visited.append([x, y, nx, ny]) # "현재 위치 -> 이동 후 위치"
                visited.append([nx, ny, x, y]) # "이동 후 위치 -> 현재 위치"
                answer += 1
            x, y = nx, ny  # 이미 지나간 경로일 경우 카운팅 X
    return answer