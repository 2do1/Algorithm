def solution(N, stages):
    answer = []
    
    people = len(stages) # 사용자의 수
    stage_dict= {} # key: 스테이지 번호, value: 실패율
    
    for stage_num in range(1, N + 1): # 1 ~ N 까지
        people_cnt = stages.count(stage_num) # 현재 스테이지에 도전하는 사용자의 수
        if people == 0: # 스테이지에 도달한 플레이어 수가 0일 경우
            stage_fail = 0
        else:
            stage_fail = people_cnt / people # 각 스테이지별 실패율
        people -= people_cnt # 남은 사용자들 
        
        stage_dict[stage_num] = stage_fail 
    
    answer = sorted(stage_dict.keys(), key=lambda x : (stage_dict[x], -x), reverse=True)
    
    return answer