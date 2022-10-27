def solution(s):
    answer = 0
    
    stack = [] # 스택

    for alphabet in s:
        if not stack: # 스택이 비어있을 경우
            stack.append(alphabet) # 스택에 추가
            
        else: # 스택이 비어있지 않을 경우     
            if alphabet == stack[-1]: # 스택 최상단과 같은 알파벳일 경우
                stack.pop()
            else: # 다른 알파벳일 경우
                stack.append(alphabet)
        
    if not stack: # 스택이 비어있을 경우, 문자열 모두 제거 했을 경우
        return 1
    else: # 스택이 비어있지 않을 경우, 문자열 모두 제거하지 못했을 경우
        return 0
    
    return answer