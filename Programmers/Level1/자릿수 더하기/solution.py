def solution(n):
    answer = 0
    n_str = str(n) # string으로 변환
    
    # for num in n_str: 
    #     answer += int(num) # str -> int 형 변환 후 더해준다.
    
    answer = sum([int(num) for num in n_str])
    
    return answer