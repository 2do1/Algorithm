def solution(cards1, cards2, goal):
    answer = "Yes"
    
    for index in range(len(goal)):
        if goal[index] in cards1:
            if cards1[0] == goal[index]:
                cards1.remove(cards1[0])
            else:
                return "No"
        elif goal[index] in cards2:
            if cards2[0] == goal[index]:
                cards2.remove(cards2[0])
            else:
                return "No"
        else:
            return "No"
        
    return answer