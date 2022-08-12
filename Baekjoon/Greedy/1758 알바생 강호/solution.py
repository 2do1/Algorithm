n = int(input()) # 사람의 수

tip_list = sorted([int(input()) for _ in range(n)], reverse=True) # 사람이 주려고 하는 팁, 내림차순 정렬

max_tip = 0 # 팁의 최댓값 
for i in range(len(tip_list)):
    if tip_list[i] - (i - 1) > 0: # 음수가 아닐 경우
       max_tip += tip_list[i] - i

print(max_tip)