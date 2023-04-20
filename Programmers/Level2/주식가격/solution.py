def solution(prices):
    answer = [0] * len(prices)
    
    stack = [] # 가격이 떨어지지 않은 가격들을 담아두는 곳
    
    for idx, price in enumerate(prices):
        if not stack: # 스택이 비어있을 경우 넣어준다.
            stack.append([idx, price]) # [인덱스, 가격]
            continue
        
        for p in stack: # 가격이 떨어지지 않은 가격들 1초 증가
            answer[p[0]] += 1
        
        if stack[-1][1] <= price: 
            stack.append([idx, price])
        else: # 주식 가격이 떨어졌을 경우
            while True:
                stack.pop()
                if not stack or stack[-1][1] <= price: # 스택이 비어있거나 현재 가격보다 이하일경우
                    break
            stack.append([idx, price])
         
    return answer