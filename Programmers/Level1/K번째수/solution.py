def solution(array, commands):
    answer = []
    
    for num_list in commands:
        i = num_list[0]
        j = num_list[1]
        k = num_list[2]
        
        arr = array[i-1:j]
        arr = sorted(arr) # 오름차순 정렬
        
        answer.append(arr[k-1])
    return answer