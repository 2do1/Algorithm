def solution(park, routes):
    answer = []
    
    start_x, start_y = 0, 0 # 시작 좌표
    row_len = len(park) # 행 길이
    col_len = len(park[0]) # 열 길이
    directions = {"N": [-1, 0], "S": [1, 0], "E": [0, 1], "W": [0, -1]} # 방향
    
    # 시작 좌표 찾기
    for index, row in enumerate(park):
        if "S" in row:
            start_x = index
            start_y = row.index("S")
            break
    
    for route in routes:
        route = route.split()
        
        nx, ny = start_x, start_y
        
        for _ in range(int(route[1])): # 현재 명령어 칸 만큼
            
            nx = nx + directions[route[0]][0]
            ny = ny + directions[route[0]][1]
            if nx < 0 or nx >= row_len or ny < 0 or ny >= col_len or park[nx][ny] == "X": # 맵 밖을 벗어나거나, 벽을 만났을 경우 명령을 무시
                nx, ny = start_x, start_y  
                break                   
        
        start_x, start_y = nx, ny
    
    answer = [start_x, start_y]
    
    return answer

# 내 처음 풀이
# def solution(park, routes):
#     answer = []
    
#     start_x, start_y = 0, 0
    
#     row_len = len(park)
#     col_len = len(park[0])
    
#     # 시작 위치 좌표 찾기
#     for i in range(row_len):
#         for j in range(col_len):
#             if park[i][j] == "S": # 시작 위치
#                 start_x = i
#                 start_y = j
#                 break
                
#     for route in routes:
#         route = route.split()
#         is_okay = True 
        
#         if route[0] == "N":
#             nx = start_x 
#             for _ in range(int(route[1])):
#                 nx = nx - 1
                
#                 if nx < 0 or nx >= row_len or park[nx][start_y] == "X":
#                     is_okay = False
#                     break
#             if is_okay:
#                 start_x = nx
#         elif route[0] == "S":
#             nx = start_x 
#             for _ in range(int(route[1])):
#                 nx = nx + 1
                
#                 if nx < 0 or nx >= row_len or park[nx][start_y] == "X":
#                     is_okay = False
#                     break
#             if is_okay:
#                 start_x = nx
#         elif route[0] == "W":
#             ny = start_y
#             for index in range(int(route[1])):
#                 ny = ny - 1
                
#                 if ny < 0 or ny >= col_len or park[start_x][ny] == "X":
#                     is_okay = False
#                     break
#             if is_okay:
#                 start_y = ny

#         else: # E
#             ny = start_y
#             for index in range(int(route[1])):
#                 ny = ny + 1
                
#                 if ny < 0 or ny >= col_len or park[start_x][ny] == "X":
#                     is_okay = False
#                     break
#             if is_okay:
#                 start_y = ny
    
#     answer = [start_x, start_y]
#     return answer