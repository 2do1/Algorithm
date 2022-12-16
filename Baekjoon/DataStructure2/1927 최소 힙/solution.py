import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap: # 비어있을 경우
            print(0)
            continue
        print(heapq.heappop(heap))
    
    else:
        heapq.heappush(heap, x)