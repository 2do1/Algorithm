def solution(numbers):
    answer = 0
    
    for num in range(10):
        if num not in numbers: # 숫자가 리스트에 없을경우
            answer += num
            
    return answer