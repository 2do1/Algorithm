n = int(input())

a = list(map(int, input().split()))

dp = [1] * 1000

for index in range(n):
    for j in range(index):
        if a[index] > a[j]:
            dp[index] = max(dp[index], dp[j] + 1)

print(max(dp))