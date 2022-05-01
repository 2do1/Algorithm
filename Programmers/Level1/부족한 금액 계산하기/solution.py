# price : 놀이기구 이용료, money: 처음 가지고 있는 금액, count: 놀이기구 이용 횟수
def solution(price, money, count):
    answer = 0
    price_sum = 0 # 총 필요한 놀이기구의 이용 금액
    
    for i in range(1, count + 1): # 1 ~ count 까지
        price_sum += price * i
    
    if money >= price_sum: # 돈이 부족하지 않을때
        answer = 0
    else: # 돈이 부족할때
        answer = price_sum - money

    return answer