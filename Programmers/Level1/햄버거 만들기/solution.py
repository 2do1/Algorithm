def solution(ingredients):
    answer = 0
    # 빵, 야채, 고기 ,빵 = 1, 2, 3, 1
    
    index = 0
    while index < len(ingredients) - 3:
        if ingredients[index] == 1:
            if ingredients[index:index + 4] == [1, 2, 3, 1]:
                del ingredients[index:index + 4]
                index -= 3
                answer += 1
              
        index += 1
    return answer