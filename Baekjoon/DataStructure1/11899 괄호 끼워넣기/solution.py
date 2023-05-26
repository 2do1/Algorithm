s = input()

stack = []

answer = 0

for bracket in s:
    if bracket == ')':
        if not stack: # '(' 괄호가 없을 경우
            answer += 1
        else: # '(' 괄호가 있을 경우
            stack.pop()
    else:
        stack.append('(')

answer += len(stack) # 나머지 괄호들

print(answer)