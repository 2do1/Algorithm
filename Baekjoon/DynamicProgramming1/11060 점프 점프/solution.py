n = int(input())
a = list(map(int, input().split()))
dp = [n + 1] * n
dp[0] = 0


# dp[i]: i번쨰까지 오려면 최소 몇 번 점프해야하는지
for i in range(n):
    length = a[i]
    for j in range(1, length + 1):
        if i + j < n: # 미로 밖을 벗어나지 않을 경우
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1: # 가장 오른쪽 끝으로 갈 수 없는 경우
    print(-1)
else:
    print(dp[n - 1])