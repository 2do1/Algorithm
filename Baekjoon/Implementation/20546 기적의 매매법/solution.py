money = int(input())

stock_price = list(map(int, input().split()))

junhyun_stock = 0 # 가지고 있는 주식
junhyun_money = money # 가지고 있는 돈
junhyun_asset = 0 # 최종 자산

sungmin_stock = 0
sungmin_money = money
sungmin_asset = 0

for price in stock_price:
    if junhyun_money >= price:
        junhyun_stock = junhyun_money // price
        junhyun_money %= price

junhyun_asset = junhyun_money + stock_price[-1] * junhyun_stock 

for index in range(3, len(stock_price)):
    if stock_price[index - 3] < stock_price[index - 2] < stock_price[index - 1] < stock_price[index]:
        sungmin_money += sungmin_stock * stock_price[index]
        sungmin_stock = 0
    elif stock_price[index - 3] > stock_price[index - 2] > stock_price[index - 1] > stock_price[index] and money >= stock_price[index]:
        sungmin_stock += sungmin_money // stock_price[index]
        sungmin_money %= stock_price[index]

sungmin_asset = sungmin_money + stock_price[-1] * sungmin_stock 

if junhyun_asset > sungmin_asset:
    print("BNP")
elif junhyun_asset < sungmin_asset:
    print("TIMING")
else:
    print("SAMESAME")