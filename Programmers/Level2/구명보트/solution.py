def solution(people, limit):
    answer = 0
    
    people = sorted(people)
    
    start, end = 0, len(people) - 1
    
    while start < end:
        if people[start] + people[end] <= limit: # 두 사람을 구명보트에 태울 수 있을 경우
            answer += 1
            start += 1
            end -= 1
        else: # 두 사람을 구명보트에 태울 수 없을 경우
            end -= 1            
    
    answer += len(people) - 2 * answer # 혼자 태워야 하는 사람들까지
    return answer