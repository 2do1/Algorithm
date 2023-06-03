n = int(input())

dp = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2

    for index in range(3, n + 1):
        dp[index] = (dp[index - 1] + dp[index - 2]) % 15746

    print(dp[n])