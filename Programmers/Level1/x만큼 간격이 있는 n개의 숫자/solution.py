def solution(x, n):
    answer = []
    # for i in range(1, n + 1): # 범위 1 ~ n
    #     answer.append(x * i)
    
    answer = [x * i for i in range(1, n + 1)]
    
    return answer