def solution(n):
    answer = 0
    
    n_one_count = bin(n)[2:].count('1') # 자연수 n을 2진수로 변환했을 때 1의 개수
    
    num = n # n의 다음 큰 숫자
    while True:
        num += 1
        one_count = bin(num)[2:].count('1') # 2진수로 변환했을 때 1의 개수
        
        if n_one_count == one_count: # 1의 개수가 같다면
            answer = num
            break
        
    return answer