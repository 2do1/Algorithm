def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        s = s[1:] + s[0] # 왼쪽으로 괄호 문자열 회전
        correct = True # 올바른 괄호인지 판단
        stack = [] # 스택 생성
        for bracket in s: # 괄호 하나씩 탐색해나가면서
            if bracket == '(' or bracket == '{' or bracket == '[': # 여는 괄호일 경우
                stack.append(bracket) 
            else: # 닫는 괄호일 경우
                if len(stack) == 0: # 스택이 비어있을 경우, 여는 괄호가 없을 경우
                    correct = False
                    break
                else: # 스택이 비어있지 않을 경우
                    temp = stack.pop() # 스택에 있는 괄호
                    if bracket == ')' and temp != '(':
                        correct = False
                        break
                    elif bracket == '}' and temp != '{':
                        correct = False
                        break
                    elif bracket == ']' and temp != '[':
                        correct = False
                        break
                
        if correct and len(stack) == 0: # 올바른 괄호 문자열일 경우
            answer += 1
    return answer