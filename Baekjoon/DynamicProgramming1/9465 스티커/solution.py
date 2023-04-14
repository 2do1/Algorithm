t = int(input()) 

for _ in range(t):
    n = int(input()) # 2n개의 스티커
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1: # n이 1일 경우
        answer = max(stickers[0][0], stickers[1][0])
        print(answer)
        continue
    
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    
    answer = -1e9
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + stickers[1][i]
    
    for row in dp: 
        answer = max(answer, max(row))
    
    print(answer)