def solution(a, b):
    answer = 0
    
    for u, v in zip(a, b): # zip()을 통해 for문에서 리스트를 동시에 사용할 수 있게 하였다.
        answer += u * v
        
    return answer