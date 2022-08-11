n, m = map(int, input().split()) #  n 행, m 열

answer = 0 # 게임의 룰에 맞게 선택한 카드에 적힌 숫자
for _ in range(n):
    num_list = list(map(int, input().split()))
    min_num = min(num_list) # 현재 행에서 가장 작은 수
    answer = max(answer, min_num) # 그 중 가장 큰 수 찾기

print(answer)