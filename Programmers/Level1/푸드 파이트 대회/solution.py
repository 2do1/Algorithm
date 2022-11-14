def solution(food):
    answer = ''
    
    food_count = []
    for i in range(1, len(food)):
        if food[i] == "0" or food[i] == "1":
            continue
        food_count.append(int(food[i]) // 2)
    
    food_arrange = ""
    for i in range(len(food_count)):
        food_arrange += food_count[i] * str(i + 1)
    
    answer = food_arrange + "0" + food_arrange[::-1]
        
    return answer