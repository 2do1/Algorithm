import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, -x)
    else:
        if not heap: # 비어있을 경우
            print(0)
            continue
        print(-1 * heapq.heappop(heap))