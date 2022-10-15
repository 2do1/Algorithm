from itertools import combinations

n, m = map(int, input().split()) # 크기가 nxn인 도시, 치킨집 m개 고르기

graph = [list(map(int, input().split())) for _ in range(n)] # 도시의 정보

home_list = [] # 집의 좌표들을 담아 놓은 곳
chicken_list = [] # 치킨집의 좌표들을 담아 놓은 곳

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집일 경우
            home_list.append([i, j])
        elif graph[i][j] == 2: # 치킨집일 경우
            chicken_list.append([i, j])

total_distance = 99999 # 도시의 치킨 거리의 최솟값
for select_chicken in combinations(chicken_list, m):
    total = 0 # 도시의 총 치킨 거리
    for home in home_list:
        chicken_distance = 99999 # 각 집에서의 치킨 거리
        for chicken in select_chicken:
            distance = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            chicken_distance = min(distance, chicken_distance)

        total += chicken_distance
        
    total_distance = min(total_distance, total)

print(total_distance)