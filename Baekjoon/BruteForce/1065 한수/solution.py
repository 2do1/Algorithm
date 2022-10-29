n = int(input())

answer = 0 # 한수의 개수
for i in range(1, n + 1):
    num = str(i) # 문자열로 변환

    if len(num) == 1 or len(num) == 2: # 한자리, 두자리 수일 경우 한수
        answer += 1
    else: # 세자리 수일 경우      
        is_hansoo = True # 한수인지의 여부

        diff = int(num[1]) - int(num[0]) # 두 수의 차이
        for i in range(1, len(num) - 1):
            if int(num[i + 1]) - int(num[i]) != diff: # 등차수열을 이루지 않을 경우
                is_hansoo = False
                break
        
        if is_hansoo: # 한수일 경우
            answer += 1
    
print(answer)

# 다른 사람의 풀이
# num = int(input())

# hansu = 0
# for i in range(1, num+1):
#     num_list = list(map(int, str(i)))
#     print(num_list)
#     if i < 100:
#         hansu += 1  # 100보다 작으면 모두 한수
#     elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#         hansu += 1  # x의 각 자리가 등차수열이면 한수
# print(hansu)