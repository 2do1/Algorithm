n = int(input()) # 도시의 개수
distances = list(map(int, input().split())) # 도로의 길이
prices = list(map(int, input().split())) # 기름 가격

prices = prices[:n-1]

# 마지막 도시의 기름 가격은 생각할필요 없다.
answer = 0

min_price = 1000000001

for index in range(n - 1):
    min_price = min(prices[index], min_price)

    answer += distances[index] * min_price

print(answer)