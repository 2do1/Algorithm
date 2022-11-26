def solution(k, scores):
    answer = []
    
    hall_of_fame = [] # 명예의전당
    for score in scores:
        if len(hall_of_fame) < k: # 초기에 k일까지
            hall_of_fame.append(score)
            answer.append(min(hall_of_fame))
        else: # k일 이후부터 
            if min(hall_of_fame) < score: # k번째 순위의 가수 점수보다 더 높으면
                hall_of_fame.remove(min(hall_of_fame))
                hall_of_fame.append(score)
                answer.append(min(hall_of_fame))
            else: # k번째 순위의 가수 점수보다 낮으면
                answer.append(min(hall_of_fame))
                
    return answer