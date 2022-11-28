from collections import Counter

def solution(k, tangerine):
    answer = 0
        
    tangerines_count = sorted(Counter(tangerine).items(), reverse=True, key=lambda x : x[1])
    for key, value in tangerines_count:
        if k <= 0: 
            break
        k -= value
        answer += 1
    
    return answer

# 시간 초과 발생
# def solution(k, tangerines):
#     answer = 0
    
#     tangerines_set = set(tangerines)
#     tangerines_count = []
    
#     for tangerine in tangerines_set:
#         tangerines_count.append(tangerines.count(tangerine))
    
#     tangerines_count = sorted(tangerines_count, reverse=True)
    
#     for tangerine in tangerines_count:
#         k -= tangerine
#         answer += 1
#         if k <= 0:
#             break
        

#     return answer