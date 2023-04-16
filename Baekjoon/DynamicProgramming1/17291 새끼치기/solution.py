n = int(input())

dp = [0] * 21
dp[0] = 1
dp[1] = 1
for index in range(2, n + 1):
    if index % 2 == 0: # 짝수일 경우
        dp[index] = dp[index - 1] * 2 - dp[index - 4] - dp[index - 5]
    else: # 홀수일 경우
        dp[index] = dp[index - 1] * 2

print(dp[n])