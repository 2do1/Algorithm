n = int(input())

cards = list(map(int, input().split()))

dp = [1] * (n + 1)

for i in range(len(cards)):
    for j in range(i):
        if cards[i] > cards[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
        # 위 if문과 같은 의미
        # if cards[i] > cards[j] and dp[j] + 1 > dp[i]:
        #     dp[i] = dp[j] + 1

print(max(dp))