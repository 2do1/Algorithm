n = int(input()) # 유제품의 수

dairy_product_list = sorted([int(input()) for _ in range(n)], reverse=True) # 유제품의 가격 비싼순으로 정렬

total_min_cost = 0 # 필요한 최소 비용
for i in range(len(dairy_product_list)):
    if i % 3 != 2: # 나머지가 2인 유제품들만 가격에 포함시키지 않는다.
        total_min_cost += dairy_product_list[i]

print(total_min_cost)