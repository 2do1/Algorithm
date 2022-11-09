def solution(lottos, win_nums):
    answer = []
    
    rank = [6, 6, 5, 4, 3, 2, 1] # 맞힌 개수(인덱스 값)에 따라 순위
    
    zero_count = 0 # 0의 개수
    correct_count = 0 # 맞힌 개수
    
    for num in lottos: 
        if num == 0: # 숫자가 0일 경우
            zero_count += 1
        elif num in win_nums: # 맞췄을 경우
            correct_count += 1
    
    min_correct = correct_count # 제일 적게 맞췄을 때 
    max_correct = correct_count + zero_count # 제일 많이 맞췄을 때
    
    answer = [rank[max_correct], rank[min_correct]]
    
    return answer

# # 처음 풀이
# def solution(lottos, win_nums):
#     answer = []
    
#     zero_count = 0 # 0의 개수
#     correct_count = 0 # 맞힌 개수
    
#     for num in lottos: 
#         if num == 0: # 숫자가 0일 경우
#             zero_count += 1
#         elif num in win_nums: # 맞췄을 경우
#             correct_count += 1
    
#     min_correct = correct_count # 제일 적게 맞췄을 때 
#     max_correct = correct_count + zero_count # 제일 많이 맞췄을 때
    
#     if max_correct == 0: # 하나도 못맞췄을 경우
#         return [6, 6]
#     else:
#         answer.append(7 - max_correct)

#     if min_correct == 0: 
#         answer.append(6)
#     else:
#         answer.append(7 - min_correct)
        
    
#     return answer