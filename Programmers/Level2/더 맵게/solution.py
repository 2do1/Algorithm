import heapq

def solution(scoville, K):
    answer = 0
    
    # heap = []
    # for s in scoville:
    #     heapq.heappush(heap, s)
    
    heapq.heapify(scoville) # 힙으로 변환 시킨다.
        
    while True:
        
        # 시간초과 발생
        # if min(scoville) >= k:
        #     break
        
        if scoville[0] >= K:
            break
        
        if len(scoville) == 1: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 경우
            return -1
    
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    
    return answer