n = int(input()) # 포도주 개수

wines = [int(input()) for _ in range(n)]

dp = [0] * (n)

if n == 1:
    print(wines[0])

elif n == 2:
    print(wines[0] + wines[1])

else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]

    for index in range(2, n):
        dp[index] = max(dp[index - 2] + wines[index], wines[index] + wines[index - 1] + dp[index - 3])
        dp[index] = max(dp[index], dp[index - 1]) # i번째를 마시지 않은 경우

    print(dp[n - 1])