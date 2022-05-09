import math

def solution(n):
    answer = 0
    
    # n_sqrt = n ** (1/2)  
    n_sqrt = math.sqrt(n) # n의 제곱근 
    
    if n_sqrt == int(n_sqrt): # n이 양의 정수 x의 제곱이라면
        # answer = (n_sqrt+1) ** 2
        answer = math.pow(n_sqrt+1, 2)
    else: # n이 양의 정수 x의 제곱이 아니라면
        answer = -1
        
    return answer

    # 다른 사람의 풀이 
    # n_sqrt = n ** (1/2)   
    # if not n_sqrt % 1:
    #     answer = math.pow(n_sqrt+1, 2)
    # else: 
    #     answer = -1