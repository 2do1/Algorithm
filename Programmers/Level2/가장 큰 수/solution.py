def solution(numbers):
    answer = ""
    
    numbers = [str(num) for num in numbers] # 숫자 -> 문자열로 변환
    
    numbers = sorted(numbers, key=lambda x : x * 3, reverse=True) # 큰 순서대로 정렬
    
    # for num in num_list:
    #     answer += str(num)
    
    answer = str(int("".join(numbers))) # 합쳐준다. 정수화한 후에 다시 문자열로 바꿔준다.
        
    return answer

# # 인덱스 에러
# def solution(numbers):
#     answer = ""
    
#     num_list = sorted(numbers, key=lambda x : (str(x)[0], str(x)[1]), reverse=True) # 내림차순 정렬
        
#     return answer

# # 시간초과
# from itertools import permutations

# def solution(numbers):
#     answer = ""
    
#     case_list = list(permutations(numbers, len(numbers))) #
#     num_list = [] # 만들 수 있는 숫자들
    
#     for case in case_list:
#         temp = "" # 각 경우마다의 수 
#         for num in case:
#             temp += str(num)
#         num_list.append(temp)
    
#     num_list = sorted(num_list, key=lambda x : int(x)) # 오름차순 정렬
    
#     answer = num_list[-1]
    
#     return answer