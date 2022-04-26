def solution(s):
    answer = True
    
    s_lower_case = s.lower() # 문자열 전체 소문자로 변경
    
    p_count = s_lower_case.count('p')
    y_count = s_lower_case.count('y')
    
    if p_count == y_count: # p 와 y 의 개수가 같을 경우
        pass
    else: # p 와 y 의 개수가 다를 경우
        answer = False
        
    return answer