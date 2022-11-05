n = int(input()) # 피연산자 수

postfix = input()

num_list = [int(input()) for _ in range(n)] # 피연산자에 대응하는 값

stack = [] # 스택
answer = 0 # 계산 결과

for char in postfix:
    char = ord(char)
    if 65 <= char <= 90: # 대문자 일경우 
        stack.append(num_list[char % 65])
    else: # 연산자일 경우
        num1 = stack.pop()
        num2 = stack.pop()

        result = str(num2) + chr(char) + str(num1)
        result = eval(result)
        
        stack.append(result)
        
answer = stack[0]

print("{:0.2f}".format(answer))