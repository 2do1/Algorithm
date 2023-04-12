from collections import deque

def solution(x, y, n):
    # 최소 연산 횟수, BFS를 통해 풀어보자
    
    # if x == y: # x랑 y가 처음부터 같은 경우가 있을 수도 있다.
    #     return 0
    
    dist = [0] * (y + 1) # 최소 연산 횟수 기록    
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        
        if x == y: # y로 변환했을 경우
            return dist[y]
            
        for nx in (x + n, x * 2, x * 3): # 세 가지 연산에 따라 탐색 진행
            if 0 <= nx <= y and not dist[nx]: # 아직 방문하지 않았고 범위 안일 경우
                dist[nx] = dist[x] + 1
                queue.append(nx)
         
    return -1 # 변환할 수 없을 경우에는