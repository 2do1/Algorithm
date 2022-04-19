def solution(x):
    answer = True
    
    digits_sum = 0 # 모든 자릿수의 합
    
    for num in str(x): # string 으로 변환 후 접근
        digits_sum += int(num) # string 형이기 때문에 int 형으로 변환
                   
    if x % digits_sum == 0: # 나누어 떨어지면 하샤드 수
        pass
    else:
        answer = False
         
    return answer