def solution(a, b):
    answer = sum([num for num in range(min(a, b), max(a, b) + 1)]) # a와 b 사이에 속한 모든 정수의 합
    
    # 다른 사람의 풀이
    # if a > b: # a가 b보다 클경우
    #     a, b = b, a
    # answer = sum([num for num in range(a, b + 1)])
        
    return answer