n = int(input()) # 지방의 수
n_list = sorted(map(int, input().split())) # 이진 탐색을 위한 정렬

m = int(input()) # 총 예산
answer = 0 # 배정된 예산들 중 최댓값인 정수

start = 1
end = max(n_list)

while start <= end:
    mid = (start + end) // 2

    total = 0 # 총합
    for n in n_list:
        if n > mid: # 요청이 상한액보다 클 경우
            total += mid
        else: # 요청이 상한액보다 작거나 같을 경우
            total += n
    
    if total <= m: # 총 예산보다 작거나 같을 경우
        start = mid + 1 
        answer = mid
    else: # 총 예산보다 클 경우
        end = mid - 1

print(answer)