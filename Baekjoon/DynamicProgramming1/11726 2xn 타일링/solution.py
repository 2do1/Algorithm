n = int(input()) # 2 x n 크기의 직사각형

dp = [0] * 1001 # dp 테이블 초기화
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])