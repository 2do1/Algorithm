n = int(input())

dp = [0] * (n + 1)

for money in range(1, n + 1):

    if money >= 7:
        dp[money] = min(dp[money - 1], dp[money - 2], dp[money - 5], dp[money - 7]) + 1
    elif money >= 5:
        dp[money] = min(dp[money - 1], dp[money - 2], dp[money - 5]) + 1
    elif money >= 2:
        dp[money] = min(dp[money - 1], dp[money - 2]) + 1
    else:
        dp[money] = dp[money - 1] + 1
        
print(dp[n])