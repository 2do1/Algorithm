from collections import deque

def solution(priorities, location):
    answer = 0
    
    index_queue = deque([num for num in range(len(priorities))]) # 인덱스, 큐에 저장
    p_queue = deque(priorities) # 우선 순위, 큐에 저장
    
    answer = 0
    while True:
        if p_queue[0] == max(p_queue):
            p_queue.popleft()
            answer += 1
            if(index_queue.popleft() == location):
                return answer    
        else:
            # popleft() append() 함수 이용
            # index_queue.append(index_queue.popleft())
            # p_queue.append(p_queue.popleft())

            # rotate 함수 이용
            index_queue.rotate(-1)
            p_queue.rotate(-1)
                       
    return answer