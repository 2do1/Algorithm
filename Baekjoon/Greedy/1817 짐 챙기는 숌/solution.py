# 책의 개수 n, 박스에 넣을 수 있는 최대 무게 m
n, m = map(int, input().split())

weight_total = 0 # 박스에 담긴 책의 총 무게
min_box_count = 0 # 필요한 박스의 개수의 최솟값

if n == 0: # 책의 개수가 0개일 때 
    pass
else: # 책의 개수가 1개 이상일 때
    book_weight_list = list(map(int, input().split())) # 책들의 무게가 담긴 리스트

    for weight in book_weight_list:
        if weight_total + weight <= m: # 책을 더 담을 수 있을 경우
            weight_total += weight
        else: # 책을 더 못담을 경우
            min_box_count += 1 # 새로운 박스를 꺼낸다.
            weight_total = 0
            weight_total += weight

    min_box_count += 1 # 마지막 상자 카운트 해준다.

print(min_box_count)

# 다른 사람의 풀이
# n, m = map(int, input().split())

# if n == 0:
#     print(0)
# else:
#     li = list(map(int, input().split()))
    
#     count = 1
#     current = 0
#     for v in li:
#         sum_value = current + v
#         if sum_value > m: 
#             current = v
#             count += 1
#         else:
#             current = sum_value
#     print(count)