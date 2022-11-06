def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복 가져온 학생이 체육복 도난당했을 경우
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for person in reserve_set:
        if person - 1 in lost_set:
            lost_set.remove(person - 1)
        elif person + 1 in lost_set:
            lost_set.remove(person + 1)
    
    answer = n - len(lost_set)
    
    return answer