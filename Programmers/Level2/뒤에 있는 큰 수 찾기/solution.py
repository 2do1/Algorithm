def solution(numbers):
    
    answer = [-1] * len(numbers) # 정답 배열을 -1로 다 초기화한다.

    stack = []
    for index, number in enumerate(numbers):
        
        if not stack or number <= stack[-1][1]: # 스택이 비어있을 경우거나 최상단에 있는 수 이하일 경우
            stack.append([index, number])
        else: # 최상단에 있는 수보다 더 클 경우
            while stack and number > stack[-1][1]:
                stack_idx, stack_num = stack.pop()
                answer[stack_idx] = number
            stack.append([index, number])
    
    return answer