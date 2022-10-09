def solution(s):
    answer = []
    count = 0 # 이진 변환의 횟수
    zero_remove_count = 0 # 제거한 0의 개수
    
    while s != "1": # s가 1이 될때까지
        one_count = s.count("1") # 1의 개수
        zero_remove_count += len(s) - one_count # 제거한 0의 개수 
        s = str(bin(one_count)[2:]) # 2진법으로 표현한 문자열
        count += 1
    
    answer.append(count)
    answer.append(zero_remove_count)
        
    return answer