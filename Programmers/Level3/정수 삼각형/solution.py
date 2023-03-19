def solution(triangle):
    answer = 0
    
    length = len(triangle)
    dp = [[0] * (length + 1) for _ in range(length + 1)]
    
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if i == 0: # 맨 왼쪽에 위치했을 경우
                dp[i][j] = dp[i - 1][j] 
            elif i == j: # 맨오른쪽에 위치했을 경우
                dp[i][j] = dp[i - 1][j - 1]
            else: # 나머지 경우
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
            
            dp[i][j] += triangle[i - 1][j - 1] # 현재 위치 값 더해준다.
    
    answer = max(dp[-1])
            
    return answer