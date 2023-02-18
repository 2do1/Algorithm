n = int(input())

soldiers = list(map(int, input().split()))

dp = [1] * (n + 1)

for i in range(len(soldiers)):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))