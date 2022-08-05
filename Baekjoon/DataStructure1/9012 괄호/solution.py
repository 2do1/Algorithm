t = int(input()) # t개의 테스트 케이스

for _ in range(t):
    parenthesis = input() # 괄호 문자열

    stack = [] # 스택
    right = True # 올바른 괄호 문자열인지 
    for char in parenthesis:
        if char == "(": # 왼쪽 괄호일 경우
            stack.append(char) 
        elif char == ")": # 오른쪽 괄호일 경우
            if len(stack) != 0: # 스택이 비어있지 않다면
                stack.pop()
            else: # 스택이 비어있을 경우
                right = False
                break

    if not stack and right:
        print("YES")
    else:
        print("NO")