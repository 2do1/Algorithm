def solution(s):
    answer = True
    stack = [] # 스택
    
    for parenthesis in s:
        if parenthesis == '(':
            stack.append(parenthesis)
        else: # 괄호가 ')'일 경우
            if len(stack) == 0: # 스택에 '('가 없을 경우 
                answer = False
            else: # 스택에 '('가 있을경우 
                stack.pop()
    
    if len(stack) != 0: # 스택에 '('가 남아있는 경우
        answer = False
            
    return answer