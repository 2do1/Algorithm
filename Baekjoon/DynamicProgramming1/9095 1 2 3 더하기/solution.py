t = int(input()) 

for _ in range(t):
    n = int(input())

    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for index in range(4, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2] + dp[index - 3]
    
    print(dp[n])