def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
    box_count = len(score) // m # 박스의 개수
    
    for index in range(box_count):
        box = score[index * m:(index + 1) * m]
        answer += min(box) * m
        
    return answer