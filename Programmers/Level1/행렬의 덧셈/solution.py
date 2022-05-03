def solution(arr1, arr2):
    answer = [[]]
    
    # 두 행렬의 덧셈을 하기 위해서는 두 행렬의 열과 행이 서로 같아야 한다.
    row_len = len(arr1)
    col_len = len(arr1[0])
    
    for i in range(row_len): # 행렬의 세로크기만큼 반복
        for j in range(col_len): # 행렬의 가로 크기만큼 반복
            arr1[i][j] += arr2[i][j] 
            
    answer = arr1
    
    return answer