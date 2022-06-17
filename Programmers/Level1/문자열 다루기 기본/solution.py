def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6: # 문자열 길이 4 또는 6일 경우
        for num in s:
            if not num.isdigit(): # 숫자가 아닐경우
                answer = False
                break
    else: # 문자열 길이 4 또는 6이 아닐 경우
        answer = False
                
    return answer