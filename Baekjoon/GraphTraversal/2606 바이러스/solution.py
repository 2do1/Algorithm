# DFS 풀이
computer_count = int(input()) # 컴퓨터의 개수
network_connet_count = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# 인접 리스트로 표현
network_list = [[] for _ in range(computer_count + 1)]

for _ in range(network_connet_count): # 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍 입력받는다.
    a, b = map(int, input().split()) 
    network_list[a].append(b)
    network_list[b].append(a)

visited = [False] * (computer_count + 1) # 컴퓨터를 방문했는지의 여부
virus_computer = 0 # 바이러스에 걸리는 컴퓨터의 수 

def dfs(v):
    global virus_computer
    visited[v] = True # 방문했음을 표시
    for i in network_list[v]:
        if not visited[i]: # 방문 하지 않았을 경우
            dfs(i)
            virus_computer += 1

dfs(1) # 1번 컴퓨터가 웜 바이러스에 걸렸을 때 
print(virus_computer)

# BFS 풀이
# from collections import deque

# computer_count = int(input()) # 컴퓨터의 개수
# network_connet_count = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# # 인접 리스트로 표현
# network_list = [[] for _ in range(computer_count + 1)]

# for _ in range(network_connet_count): # 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍 입력받는다.
#     a, b = map(int, input().split()) 
#     network_list[a].append(b)
#     network_list[b].append(a)

# visited = [False] * (computer_count + 1) # 컴퓨터를 방문했는지의 여부
# virus_computer = 0 # 바이러스에 걸리는 컴퓨터의 수 

# def bfs(v):
#     global virus_computer
#     queue = deque([v]) # 큐 생성
#     while queue: # 큐 안에 값이 다 없어질 때 까지
#         computer = queue.popleft() 
#         visited[computer] = True # 방문했음을 표시

#         for i in network_list[computer]:
#             if visited[i] == False: # 방문하지 않았으면
#                 visited[i] = True
#                 queue.append(i) # 큐에 추가
#                 virus_computer += 1  
#     print(virus_computer)

# bfs(1) # 1번 컴퓨터가 웜 바이러스에 걸렸을 때 