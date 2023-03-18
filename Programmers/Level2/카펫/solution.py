def solution(brown, yellow):
    answer = []
              
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) + 4 == brown:
                return [yellow // i + 2, i + 2]
        
    return answer