def solution(n):
    answer = 0
    
    for num in range(2, n + 1): # 2 ~ n까지
        prime = True # 소수인지의 여부를 알려주는 변수
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        
        if prime: # 소수라면
            answer += 1
        
    return answer