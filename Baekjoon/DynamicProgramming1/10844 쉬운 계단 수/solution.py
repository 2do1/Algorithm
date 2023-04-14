n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
# dp[자릿수][맨 뒤에 오는 수]

# 1의 자릿수 값을 미리 채워주자. 
for index in range(1, 10):
    dp[1][index] = 1

for i in range(2, n + 1): # 한자리수부터 n자리수 까지
    for j in range(10): # 0 ~ 9
        if j == 0: # 0일 경우, 0은 맨 앞자리에는 올 수 없다.
            dp[i][j] = (dp[i - 1][1]) % 1000000000
        elif j == 9: # 9일 경우, 9는 옆에 8만 올 수 있다.
            dp[i][j] = (dp[i - 1][8]) % 1000000000
        else: # 1 ~ 8 까지의 숫자일 경우
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000


print(sum(dp[n]) % 1000000000)