n = int(input()) # 상근이가 갖고 있는 카드의 개수
card_list = sorted(map(int, input().split())) # 오름차순 정렬

m = int(input())
num_list = list(map(int, input().split())) # m개의 정수

for num in num_list:
    start = 0
    end = len(card_list) - 1
    have = False # 갖고있는지의 여불

    while start <= end:
        mid = (start + end) // 2

        if card_list[mid] == num: # 상근이가 갖고 있을 경우
            have = True
            break
        elif card_list[mid]  > num: 
            end = mid - 1
        else:
            start = mid + 1
    
    if have: # 갖고있을 경우
        print(1, end=' ')
    else: # 갖고있지 않을 경우
        print(0, end=' ')