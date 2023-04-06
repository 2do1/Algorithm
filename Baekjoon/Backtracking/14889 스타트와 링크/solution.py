

# 조합을 한번 해서 두개로 나눠준 뒤 각각에 대해서도 조합을 진행
def dfs(depth, start):
    global answer
    if depth == n // 2: # 두개로 나누었을 경우
        
        power_start = 0 # 스타트 팀
        power_link = 0  # 링크 팀

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power_start += stats[i][j]
                elif not visited[i] and not visited[j]:
                    power_link += stats[i][j]
        
        answer = min(answer, abs(power_start - power_link))
        return 
    
    for index in range(start, n):
        if not visited[index]:
            visited[index] = True
            dfs(depth + 1, index + 1)
            visited[index] = False


n = int(input())

stats = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

answer = 2e9 # 팀의 능력치 차이의 최솟값 

dfs(0, 0)
print(answer)