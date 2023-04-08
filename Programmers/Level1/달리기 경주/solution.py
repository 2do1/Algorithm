def solution(players, callings):
    answer = []
    
    player_dic = {} # (플레이어, 등수)
    rank_dic = {} # (등수, 플레이어))
    
    for index, player in enumerate(players):
        player_dic[player] = index
        rank_dic[index] = player
        
    for call in callings:
        call_player_rank = player_dic[call] # 불린 사람 순위
            
        front_call_player_rank = call_player_rank - 1 # 앞에있는 사람 순위
        front_call_player = rank_dic[front_call_player_rank] # 앞에 있는 사람
        
        # 바꿔준다.
        player_dic[call] = front_call_player_rank
        player_dic[front_call_player] = call_player_rank
        
        rank_dic[call_player_rank] = front_call_player
        rank_dic[front_call_player_rank] = call
    
    
    answer = list(rank_dic.values())
    
    return answer