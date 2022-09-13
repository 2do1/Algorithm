n = int(input()) # 가로의 길이가 n

dp = [0] * (n + 1) # dp 테이블 초기화

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[n])