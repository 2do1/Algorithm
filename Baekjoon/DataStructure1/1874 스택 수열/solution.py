n = int(input())

stack = []
answer = []
cnt = 1

for _ in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else: # 스택 수열을 만들 수 없을 경우
        break

if stack: # 만들수 없을 경우
    print("NO")
else:
    for operand in answer:
        print(operand)