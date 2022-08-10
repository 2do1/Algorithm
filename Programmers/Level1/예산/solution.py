def solution(d, budget):
    answer = 0
    
    d = sorted(d) # 오름차순으로 정렬
    
    total = 0 # 총 가격
    for price in d:
        total += price
        if budget >= total: # 예산 내의 범위라면
            answer += 1
        else: # 예산 밖으로 벗어난다면
            break
        
    return answer