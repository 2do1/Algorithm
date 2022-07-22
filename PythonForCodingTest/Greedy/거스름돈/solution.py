coin_list = [500, 100, 50, 10] # 거스름돈으로 사용할 동전

n = int(input()) # 거슬러 줘야 할 돈 n원
answer = 0 # 거슬러 줘야 할 동전의 최소 개수

for coin in coin_list:
    answer += n // coin  # 값이 큰 동전부터 최대한 많이 거슬러 준다.
    n %= coin

print(answer)