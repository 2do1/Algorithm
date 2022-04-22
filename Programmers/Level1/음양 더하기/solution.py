def solution(absolutes, signs):
    answer = 0
    
    for num, sign in zip(absolutes, signs):
        if sign: # True이면
            answer += num   # 그대로 더해준다.
        else:
            answer -= num   # -붙여서 더해준다.
        
    return answer