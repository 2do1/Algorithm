def solution(arr, divisor):
    answer = []
    
    answer = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0]
#     for i in range(len(arr)): 
#         if arr[i] % divisor == 0: # 원소가 divsor로 나누어 떨어지는 경우
#             answer.append(arr[i]) # 리스트에 원소 추가
            
    if len(answer) == 0: # 나누어 떨어지는 원소가 아무것도 없을 경우
        answer.append(-1) 
        return answer # 오름차순 정렬 해줄 필요 없기 때문에, 바로 리턴해준다.
    
    answer.sort() # 오름차순 정렬 후 리턴해준다.
    return answer