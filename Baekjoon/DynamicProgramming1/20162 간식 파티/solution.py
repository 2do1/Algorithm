n = int(input())

snacks = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(len(snacks)):
    dp[i] = snacks[i]
    for j in range(i):
        if snacks[i] > snacks[j]:
            dp[i] = max(dp[i], dp[j] + snacks[i])

print(max(dp))