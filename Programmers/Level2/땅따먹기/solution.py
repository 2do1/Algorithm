def solution(land):
    answer = 0  
    
    row = len(land) # 행길이
    col = len(land[0]) # 열 길이 
    
    for i in range(1, row):
        for j in range(col): 
            land[i][j] += max(land[i - 1][j + 1:] + land[i - 1][:j])

    answer = max(land[-1])
            

    return answer