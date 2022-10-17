r, c, w = map(int, input().split()) # r번째 줄, c번째 수, w번째 수

dp = [[0] * 31 for _ in range(31)] # dp 테이블 초기화

for i in range(31):
    for j in range(i + 1):
        if i == j or j == 0: # nCn이나 nC0일 경우
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0 # 해당하는 합
for i in range(r - 1, r + w - 1):
    for j in range(c - 1, c + i - r + 1):
        answer += dp[i][j]

print(answer)