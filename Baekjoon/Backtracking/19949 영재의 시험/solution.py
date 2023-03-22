exam_answers = list(map(int, input().split())) # 시험의 정답

case = [1, 2, 3, 4, 5] # 5지 선다
stack = []
answer = 0 # 5점 이상일 경우

def dfs():
    global answer
    if len(stack) >= 3:
        if stack[-3:] == [stack[-1]] * 3: # 3개의 연속된 문제의 답이 같을 경우
            return

    if len(stack) == 10: # 정답을 10개 골랐을 경우
        total = 0
        for index in range(10):
            if stack[index] == exam_answers[index]:
                total += 1

        if total >= 5:
            answer += 1         
        return
    
    for index in range(5):
        stack.append(case[index])
        dfs()
        stack.pop()

dfs()

print(answer)