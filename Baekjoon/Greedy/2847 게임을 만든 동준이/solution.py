n = int(input()) # 레벨의 수, n
clear_score_list = [] # 각 레벨당 클리어 했을 때의 점수를 담을 리스트
minus_total = 0 # 총 감소시켜야하는 점수

for _ in range(n):
    clear_score_list.append(int(input())) 

last_level_clear_score = clear_score_list[-1] # 가장 마지막 레벨을 클리어하면 얻는 점수

for i in range(len(clear_score_list) - 2, -1, -1): # 역순으로 리스트에 접근
    if clear_score_list[i] >= last_level_clear_score: # 이전 레벨의 클리어 점수가 다음 레벨 클리어 점수보다 크거나 같을 때 
       minus_total += clear_score_list[i] - (last_level_clear_score - 1) # 다음 레벨 클리어 점수보다 -1만큼 작게 마이너스 해준다.
       clear_score_list[i] = last_level_clear_score - 1 # 다음 레벨 클리어 점수보다 -1 작게 설정.
       last_level_clear_score = clear_score_list[i] # 클리어 점수 업데이트  
    else:  # 이전 레벨의 클리어 점수가 다음 레벨 클리어 점수보다 작을 때
        last_level_clear_score = clear_score_list[i] # 클리어 점수 업데이트
       
print(minus_total)

# 다른 사람 풀이
# n = int(input()) # 레벨의 수, n
# clear_score_list = [] # 각 레벨당 클리어 했을 때의 점수를 담을 리스트
# minus_total = 0 # 총 감소시켜야하는 점수

# for _ in range(n):
#     clear_score_list.append(int(input())) 

# for i in range(n - 1, 0, -1): # 역순으로 접근
#     if clear_score_list[i - 1] >= clear_score_list[i]: 
#         minus_total += (clear_score_list[i - 1] - clear_score_list[i]) + 1 # 잠수를 (레벨 차이 + 1) 만큼 감소
#         clear_score_list[i - 1] = clear_score_list[i] - 1 # 이전 레벨은 현재 레벨보다 작은 점수 부여

# print(minus_total)