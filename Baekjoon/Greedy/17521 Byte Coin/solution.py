n, w = map(int, input().split()) # 요일 수 n, 초기 현금 w

price_list = [int(input()) for _ in range(n)] # 바이트 코인 가격

coins = 0 # 총 코인 개수
for i in range(len(price_list) - 1):
    if price_list[i] < price_list[i + 1]: # 다음날 코인 가격이 더 비싸다면
        coins = w // price_list[i] # 산 코인의 개수
        w %= price_list[i] # 코인을 사고 남은 돈
        w += coins * price_list[i + 1] # 코인 팔기

print(w) # 현급의 최댓값 출력