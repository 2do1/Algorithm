def solution(n):
    answer = 0
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i <= 2: # i가 2이하일 경우
            dp[i] = i
        else: # i가 3이상일 경우
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    answer = dp[n]
    return answer

# 처음 풀이 
# def solution(n):
#     answer = 0
#     dp = [0] * 2001 # dp 테이블 초기화
#     dp[1] = 1
#     dp[2] = 2
    
#     for i in range(3, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        
#     answer = dp[n]
#     return answer