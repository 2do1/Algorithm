num_list = list(map(int, input().split())) # 다섯 개의 자연수

# 적어도 세 개로 나누어 지는 가장 작은 자연수
multiple_num = min(num_list) # 다섯 개의 자연수 중 가장 작은 값 부터
while True:
    count = 0 # 나누어 지는 횟수
    for num in num_list:
        if multiple_num % num == 0: # 나누어 떨어지는 경우
            count += 1
    
    if count > 2: # 적어도 대부분의 배수일 경우
        print(multiple_num)
        break
    else:
        multiple_num += 1 

# 처음 풀이
# num_list = list(map(int, input().split())) # 다섯 개의 자연수

# # 적어도 세 개로 나누어 지는 가장 작은 자연수
# multiple_num = 1 
# while True:
#     multiple = False # 적어도 대부분의 배수인지의 여부
#     count = 0 # 나누어 지는 횟수

#     for num in num_list:
#         if multiple_num % num == 0: # 나누어 떨어지는 경우
#             count += 1
#             if count == 3: # 적어도 세 개로 나누어질 경우
#                 multiple = True
#                 break
    
#     if multiple: # 적어도 대부분의 배수일 경우
#         print(multiple_num)
#         break
#     else:
#         multiple_num += 1