while True:
    n, m = map(int, input().split()) # n주 동안 매주 상위 m명의 랭킹 정보

    if n == 0 and m == 0: # 마지막 인풋일 경우
        break

    rank_dict = {} # 랭킹 정보를 담아놓은 딕셔너리
    for _ in range(n):
        rank_list = list(map(int, input().split())) # 주마다 랭킹 정보
        for rank in rank_list:
            if rank in rank_dict: # 이미 존재하는 참가자일 경우
                rank_dict[rank] += 1
            else: # 새로운 참가자일 경우
                rank_dict[rank] = 1
    
    score_list = sorted(rank_dict.values(), reverse=True) # 점수 기준으로 내림차순 정렬
    second = score_list[1] # 2등 선수의 점수

    second_num_list = [] # 2등 선수들의 번호 
    for key, value in rank_dict.items():
        if value == second: # 2등 선수의 점수일 경우
            second_num_list.append(key)
    
    second_num_list.sort() # 오름차순 정렬
    print(*second_num_list)