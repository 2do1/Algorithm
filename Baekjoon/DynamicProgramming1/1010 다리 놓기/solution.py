t = int(input()) # 테스트 케이스의 개수

for _ in range(t):
    n, m = map(int, input().split()) # 서쪽과 동쪽에 있는 사이트의 개수 n, m. n <= m

    dp = [[0] * 30 for _ in range(30)]

    for i in range(m + 1):
        for j in range(i + 1):
            if i == j or j == 0: # nCn 또는 nC0일 경우
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    print(dp[m][n])