def solution(participant, completion):
    answer = ''
    
    # 시간 초과 발생
    # for person in participant:
    #     if person not in completion:
    #         answer = person
    #         break
    #     else:
    #         completion.remove(person)
    
    # 두 리스트 오름차순 정렬
    participant.sort()
    completion.sort()
    
    for part, comp in zip(participant, completion):
        if part != comp: # 다를 경우
            return part
            
    # 끝까지 비교 해도 다른 경우가 없는 경우, 참가자 리스트 마지막 인덱스에 존재
    return participant[-1]