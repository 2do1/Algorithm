n = int(input())

a = list(map(int, input().split()))
dp = [1] * 1001

for i in range(len(a)):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))