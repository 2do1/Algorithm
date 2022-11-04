def solution(citations):
    answer = 0
    
    citations = sorted(citations) # 오름차순 정렬
    
    for i in range(0, max(citations) + 1): # 0 ~ 제일 많이 인용된 수
        h = 0 
        for num in citations:
            if num >= i: 
                h += 1
        
        if h >= i: 
            answer = max(answer, i)
            
    return answer