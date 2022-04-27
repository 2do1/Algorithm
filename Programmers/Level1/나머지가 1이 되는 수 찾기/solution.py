def solution(n):
    answer = 0
    
    for num in range(2, n): # 1로 나누는것은 의미 없기 때문에 2부터 시작
        if n % num == 1: # 나머지가 1일 경우
            answer = num
            break
            
    return answer