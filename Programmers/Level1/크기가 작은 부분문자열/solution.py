def solution(t, p):
    answer = 0
    
    index = len(p)
    
    for index in range(len(t) - len(p) + 1):
        if int(t[index:index + len(p)]) <= int(p):
            answer += 1
    
    return answer