n = int(input())

dp = [0] * 10001

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    for index in range(3, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    
    print(dp[n])