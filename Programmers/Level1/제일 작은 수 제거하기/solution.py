def solution(arr):
    answer = arr
    
    if len(arr) >= 2: # 배열 길이가 2 이상일 경우
        answer.remove(min(arr))
    else: # 배열 길이가 1일 경우
        answer = [-1]
        
    return answer