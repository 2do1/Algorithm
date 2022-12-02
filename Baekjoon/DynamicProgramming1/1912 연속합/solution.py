n = int(input()) # n개의 정수

numbers = list(map(int, input().split()))

dp = [0] * n
dp[0] = numbers[0]

for index in range(1, n):
    dp[index] = max(numbers[index], dp[index - 1] + numbers[index])

answer = max(dp)
print(answer)