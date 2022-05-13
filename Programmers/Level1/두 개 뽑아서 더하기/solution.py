from itertools import combinations

def solution(numbers):
    answer = set() # 집합 선언
    
    pick_cases = list(combinations(numbers, 2)) # 조합, 숫자 2개 선택
    for case in pick_cases:
        answer.add(sum(case)) # 뽑은 두 숫자의 합을 집합에 넣어준다. 집합을 이용해 중복제거
    
    answer = sorted(answer) # 오름차순 정렬 후 리스트로 리턴해준다.
    return answer
 
#     처음 풀이
#     answer = []
#     pick_cases = list(combinations(numbers, 2)) # 조합, 숫자 2개 선택
    
#     for case in pick_cases:
#         case_sum = sum(case) # 뽑은 두 숫자의 합
#         if case_sum not in answer: # 중복되는 값 방지하기 위해 리스트에 없을 경우에만 넣어준다.
#             answer.append(sum(case))
            
#     answer.sort() # 오름차순 정렬
    
#     다른 사람의 풀이
#     이중 for문을 이용해 숫자 2개 선택
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))