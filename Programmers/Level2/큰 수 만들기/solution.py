def solution(number, k):
    answer = 0
    
    number = list(map(int, number))
     
    stack = [] # 스택 자료구조 이용
    cnt = 0 # 몇 개 제거했는지 카운팅
    for num in number:
        # 스택이 비어있지 않고, 스택이 있는 수가 작을 때, 아직 K개의 수를 제거하지 않았을 경우
        while stack and stack[-1] < num and k != cnt: 
            stack.pop()
            cnt += 1
        stack.append(num)
    
    
    if cnt != k: # 아직 k개의 수만큼 제거하지 않았을 경우
        stack = stack[:-k]

    answer = ''.join(map(str, stack))
    return answer