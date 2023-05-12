t = int(input())

for _ in range(t):
    n = int(input()) # 징검다리의 수 

    #최대로 하기 위해서는 1칸씩 건너뛰어야함
    start = 1
    end = n
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if mid * (mid + 1) <=  2 * n:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end  = mid - 1
    print(answer)