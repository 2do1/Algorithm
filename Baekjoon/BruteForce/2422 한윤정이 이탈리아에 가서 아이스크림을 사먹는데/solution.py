n, m = map(int, input().split()) # 아이스크림 종류 n, 섞어먹으면 안되는 조합 개수 m

ice_cream_list = [i for i in range(1, n + 1)] # 아이스크림 종류
not_mix_list = [[True for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split()) # 먹으면 안되는 조합
    not_mix_list[a - 1][b - 1] = False 
    not_mix_list[b - 1][a - 1] = False

answer = 0
for i in range(n - 2):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not_mix_list[i][j] and not_mix_list[i][k] and not_mix_list[j][k]: # 섞어먹을 수 있을 경우
                answer += 1
print(answer)

# 시간 초과
# from itertools import combinations

# n, m = map(int, input().split()) # n: 아이스크림 종류의 수, m: 섞어먹으면 안 되는 조합의 개수

# ice_cream_list = [i for i in range(1, n + 1)] # 아이스크림 종류
# not_mix_list = [list(map(int, input().split())) for _ in range(m)] # 섞어먹으면 안 되는 조합의 번호

# select_list = list(combinations(ice_cream_list, 3)) # 아이스크림을 3개 선택하는 모든 경우의 수

# answer = 0
# for select in select_list:
#     choose = False # 선택 가능한 방법인지의 여부 
#     for not_mix in not_mix_list:
#         select = list(select) # 튜플 -> 리스트화
#         if list(set(select) - set(not_mix)) == select: # 섞어먹으면 안 되는 조합이 없을 경우
#             choose = True
#             break
    
#     if choose: # 선택 가능한 방법이면
#         answer += 1

# print(answer)