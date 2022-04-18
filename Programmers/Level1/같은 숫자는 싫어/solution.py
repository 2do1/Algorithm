def solution(arr):
    answer = []
    answer.append(arr[0]) # 배열의 첫 원소를 넣어준다.

    for i in range(1, len(arr)): # 배열의 두번째 원소부터 비교
        if answer[-1] != arr[i]: # 연속되는 숫자가 아닌 경우
            answer.append(arr[i])
        else: # 연속되는 숫자가 있는 경우
            continue
            
    return answer