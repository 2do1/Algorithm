# 다른 사람 풀이
# def solution(n, m, section):
#     answer = 0
#     painted_idx = 0 # 칠해진 인덱스 위치
    
#     for s in section:
#         if s >= painted_idx: 
#             painted_idx = s + m        
#             answer += 1
#     return answer

# 내풀이
def solution(n, m, section):
    answer = 0
    
    visited = [True] * (n + 1) # 칠했는지의 여부 확인
    
    for s in section:
        visited[s] = False
    
    for s in section:
        if not visited[s]:
            for j in range(m):
                if s + j <= n and not visited[s + j]: # 범위를 벗어나지 않고 아직 칠하지 않았을 경우
                    visited[s + j] = True
            answer += 1
    
    return answer