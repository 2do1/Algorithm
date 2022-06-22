t = int(input()) # 테스트케이스의 개수

for _ in range(t):
    # j는 사탕의 개수, n은 상자의 개수
    j, n = map(int, input().split())
    box_size_list = [] # 상자의 크기들이 담긴 리스트
    min_need_box = 0 # 상자를 최소한으로 쓸 때의 상자 개수
    for _ in range(n):
        # r은 상자의 세로 길이, c는 상자의 가로 길이
        r, c = map(int, input().split())
        box_size_list.append(r * c)
    
    box_size_list = sorted(box_size_list, reverse=True) # 내림차순 정렬
    for box_size in box_size_list: # 큰 상자 순서대로 접근
        j -= box_size
        min_need_box += 1
        if j <= 0: # 남은 사탕이 없을 경우
            break

    print(min_need_box) 