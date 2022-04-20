def solution(num):
    count = 0 # 작업 횟수 세기
    
    while num != 1: # 1이 될 때까지 반복
        if num % 2 == 0: # 짝수일 경우
            num /= 2 
        else: # 홀수일경우
            num = num * 3 + 1
        count += 1 # 작업 count
        
        if count == 500:
            count = -1
            break

    return count