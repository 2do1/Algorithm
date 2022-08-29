n, m = map(int, input().split()) # 떡의 개수 n, 요청한 떡의 길이 m

tteok_list = list(map(int, input().split())) # 떡의 개별 놆이

start = 0 # 시작점
end = max(tteok_list) # 끝점, 가장 긴 떡의 길이

answer = 0 # 절단기에 설정할 수 있는 높이의 최댓값
while start <= end:
    mid = (start + end) // 2
    
    total = 0 # 절단기로 잘린 떡의 총 길이
    for tteok in tteok_list:
        if tteok > mid: # 떡이 절단기의 높이보다 길 경우
            total += tteok - mid

    if total < m: # 잘린 떡의 총 길이가 부족할 경우
        end = mid - 1
    else: # 잘린 떡의 총 길이가 충분할 경우
        answer = mid # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(answer) 