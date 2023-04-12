from collections import deque

def solution(progresses, speeds):
    answer = []
    
    p_queue = deque(progresses)
    s_queue = deque(speeds)
    
    while True:
        if not p_queue: # 큐가 비어있을 경우
            break
            
        for _ in range(len(p_queue)): # 작업을 진행한다.
            progress = p_queue.popleft()
            speed = s_queue.popleft()
            
            p_queue.append(progress + speed)
            s_queue.append(speed)
        
        if p_queue[0] >= 100: # 진도가 100프로일 이상일 때
            total = 0 # 이번에 배포될 기능 개수
            while True:
                if not p_queue or p_queue[0] < 100: # 큐가 비어있거나, 진도가 100%가 안됐을 경우
                    break
                p_queue.popleft()
                s_queue.popleft()  
                total += 1
            answer.append(total)
            
    return answer